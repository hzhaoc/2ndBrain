This topic will introduce **Tomasulo’s Algorithm** and how it **schedules instructions** (mainly: issue, execute, write) out-of-order (with Instruction Queue/IQ, Reservation Stations/RS, RAT). Note here [[ILP - ILP & Deps.#Approach 2 Register renaming|Register renaming with RAT]] is also used to remove false deps. So after this, the only remaining theoretical constraint for ILP I think is [[ILP - ILP & Deps.#Data Dependencies|true data dependencies ]] which is inevitable.

## Out-of-Order overview
- Fetch, Decode, Issue are STILL **in-order**.
- Execute, Write (+ Broadcast) are here **out-of-order**
- Commit should STILL be **in-order** (however in Tomasulo's Algo, it is OOO, and it's solved using [[ILP - OOO EXE w Reorder Buffer|Reorder Buffer]]).
![[out-of-order overview in pipeline.png|500]]
Think of it as a pipeline. **CPI is limited by weakest link**. For example if Decoder can decode 2 inst / cycle while others do 4 inst / cycle, overall processor CPI is limited to 2 inst / cycle.

## Overview to improve IPC
-	control deps => [[ILP - Ctrl Deps. - Branch Predict|branch  prediction]]
-	false data deps => [[ILP - ILP & Deps.#Approach 2 Register renaming|register renaming]]/duplicate register values
-	true data deps => out-of-order execution (i personally think true data deps. is the only theoretical limit to OOO)
-	structural deps => invest in wider-issue processor (that can issue more insts per cycle)

## Tomasulo's Algorithm
One of the techniques created in 1960s for out-of-order inst execution. Used in the old IBM 360. It determines which insts have INPUTS READY. It includes register renaming. It is very similar to what we have today (as of 2021). The differences today's used from Tomasulo's algo are:
1. All instructions use the algorithm, not just floating point ones.
2. Hundreds of instructions are considering when performing out-of-order execution and register renaming, not just a few.
3. There is now support for exception handling.

- Overview
	- **Instruction Queue (IQ)** stores instructions from fetch unit
	- IQ **Issues** insts:
		- for arithmetic insts: (_out-of-order, our FOCUS_)
			- inst goes to **Reservation Station (RS)**, waiting for execution
			- RS **Dispatches** insts to arithmetic units such as ADD, MUL
			- values from arithmetic units are **Broadcast** to [[Storage Hierarchy#Register|Registers]] & RS
		- for memory insts: (_LB&SB execute in-order, not the algo's focus here, modern techniques  (2021) improves this_)
			- compute address
				- for load inst
					- data addr goes to **Load Buffer (LB)**
					- consult [[Storage Hierarchy|Memory]], load data to Registers
				- for store inst
					- data & data addr go to **Store Buffer (SB)**
					- all values on Broadcast Bus will also go to store before store to Mem
					- store to Memory
	- ![[Instruction -Tomasulo's Algo.png|500]]

##### Instruction to Broadcast Path
- Data Manipulation Path:
-> Instruction Queue 
→ Reservation stations (values come from the registers)
→ Execution Units(Adders and Multiplier)
→ Broadcast on the Bus

- Load/Store Path:
-> Instruction Queue 
→ Adder (for PC) 
→ Load or Store Buffer 
→ Memory 
→ Broadcast on the bus 

- Issue = instructions exit the queue and go to either the RS or the PC-Adder. 
- Dispatch = Instruction exits RS and goes to either the Adder or the Multiplier for execution.
- Write Result or Broadcast = the instruction exits the Adder or the Multiplier and is put on the bus.

## Issue
1. **Next** instruction from the IQ-instructions are issued (_in program order)_
2. Determine origin of inputs (_from registers or from other insts that haven't broadcast values_)
3. Get free RS of the correct kind (_ADD, MUL, etc. _)- if there are no free RS, the instruction needs to wait for an open RS.
4. Put instruction in the appropriate RS
5. Tag the destination register - this register will hold the result of the instruction and all other instructions will be able to access this result if necessary.

##### Issue Example - Steps for Issue
1. Take **next** instruction from IQ
2. Look in the RAT 
	- if RAT has a value for the register - use the register pointed to
	- if RAT does not have a value - directly look in the register file
3. Reservations Stations - some are adders and some are multipliers 
	- if an RS is open - use it 
	- if an RS is not available - wait for one to be open
4. Store in the RAT the register that holds the result of the instruction.

example graph (note how F1 inst is renamed/overwritten from RS4 to RS3)
![[Tomasulo's Algo - inst issue eg.png|600]]

## Dispatch
Dispatch needs to **latch** the results and determine which instructions are ready to execute.
1. Free the RS
2. Match the broadcast tag with the operations in the R
3. Insert the value in the appropriate RS
4. Once an RS has all of its required inputs - it can execute in the Adder or the Multiplier.
5. When the result is ready from the Adder or the Multiplier, broadcast it on the bus.
6. Repeat 1-5

example graph
- RS1 with value is Broadcast in
- free RS1 (where the broadcast value gets from)
![[inst dispatch 1.png]]
- replace RS1 with actual value
- dispatch inst in RS that has obtained all inputs (values) to execute
![[inst dispatch 2.png]]
- repeat

**If more than 1 instruction is ready for execution**
Which instruction should be dispatched first.
- Can choose the oldest instruction first
- The instruction with the most dependencies goes first (how many instructions are waiting for this result). this is difficult to implement in hardware
- Random selection

## Broadcast
1. Put the **tag** and the **result** on the bus.
2. Write the result to the register file.
3. Update the RAT. An empty RAT entry means the value is ready in the register file
4. Free the reservation station (change the valid bit)

example
![[instruction broadcast.png|500]]

##### What if there is More the 1 Broadcast Ready?
How to decide which result is broadcast first?
1. A separate bus for each arithmetic unit - this increases the hardware needs
2. Give priority to the slower unit - the slower unit instructions will most likely have more dependencies. The multiplication/divide unit takes more cycles to complete - so it is usually given priority.

##### Broadcasting a Stale Result
A result is stale if it no longer has an entry in the RAT (because it gets renamed to another RS block). A stale result is broadcast and placed in the appropriate RS entry. The RAT is not altered because any future instructions will not use this value. **Remember this on OMSCS CS 6290 Summer 2021 Midterms and Finals**

## Review
For each instruction: 
- Issue
- Capture (values from Broadcast Bus)
- Dispatch
- Write Result

In each cycle (at the same time)
- Issue
- Capture (values from Broadcast)
- Dispatch (one for each arithmetic unit)
- Write results (for different instructions)

1. Can same-cycle same-instruction issue->dispatch be done? 
	- Typically **no**. It depends on the processor. Issue time is shorter than the cycle time, so there can be time to do the dispatch.  But the cycle should be as short as possible, so it should not be feasible.
2. Can same-cycle same-instruction capture->dispatch be done? 
	- typically **no**
3. Can same-cycle broadcast->issue to same RS be done ? 
	- **Yes**. It requires additional logic to work. (broadcast first, issue second)
4. Can the RS free and re-alloc be in  same cycle?
	- No. The RS block that is dispatched to EXE has to wait until result value is Broadcast back and then do **free** (so this RS **holds the inst name **during the time). Usually **1 cycle** after free, the same RS block then can be re-alloc.

##### Load and Store Instructions
There can be data dependencies through memory.
- RAW occurs when a store word to a memory location occurs after a load word of that same memory location.
- WAR occurs when a load word to a memory location occurs after a store word.
- WAW occurs when there are two store words to the same memory location.

These need to obeyed or eliminated by:
- (Tomasulo's algo) Doing loads and stores in-order
- (modern processor) Identify dependencies and reorder. Memory register reordering is more complicated than normal register reordering.