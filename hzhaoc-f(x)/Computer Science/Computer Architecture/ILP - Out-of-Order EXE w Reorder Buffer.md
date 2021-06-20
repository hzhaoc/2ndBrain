This topic describes how to handle exceptions with an additional **Reorder Buffer** (**ROB**) table to solve Tomasulo's algorithm's **WB to Reg disorder issue** (caused by exception handling , branch mispred, mem page fault, etc). Today's modern processor (2021) mostly use ROB.
- Notes:
	-	RAT is **current state** where registers point to  (Reg file? ROB?) at the time of the scheduling state. And Reserve Stations may have stale Reg operand names that are intermediary values.

##### Exceptions in Out-of-Order Execution
The major drawback of Tomasulo’s algorithm is that it does not handle exceptions very well. When an exception occurs in OOO (out-of-order) processors the instructions after the exception producing instruction have been executed, resulting in incorrect outcomes **(the instruction back from exception handling reads incorrect input)**.

##### Branch Mispredictions in OOO Execution
Tomasulo’s algorithm does not handle branch mispredictions in OOO processors well. On one hand, by the time exception handling is done for validation branch prediction correctness, wrong issued insts have already executed. On the other hand, those wrong insts may include _Phantom Exceptions_.

_Phantom Exceptions_:
-	if a branch is mispredicted, a number of instructions are executed before the misprediction is detected. It is possible to generate an exception within these executed instructions, now the processor must recover from an exception that should not have occurred as well as the misprediction. **Exception handling should not occur until the processor is sure they are not phantom exceptions**

##### Correct OOO Execution
-  Execute OOO
-  Broadcast OOO
-  Deposit values in registers **In-Order** (in Tomasulo's it is OOO). This can be achieved with a **ReOrder Buffer**.

A **ReOrder Buffer (ROB)** remembers the program order and keeps the results until it is safe to write  them.

#####  ROB Table
ROB table has three fields:
- Reg
- Value
- Done bit

Insts are kept **in program order**. There are two pointers associated with the ROB:
- **Commit** tells which inst is to be completed next
- **Issue** tells where the next issued inst is to be placed in the ROB

##### ROB Issue
How the ROB interacts with the IQ, RS, Regs, and the RAT.
1. Get Inst from IQ
2. Get a free RS
3. Get next ROB entry at Issue pointer, then **Issue Pointer ++**
4. Rename the src reg in RAT to dest reg which **points to the ROB entry** instead of **RS** (RS can be free the moment after dispatched to EXE, RS does not have to hold reg name anymore, ROB does it)

##### ROB Dispatch
1. Find results where the tags match.
2. Only insts where all the inputs are ready are considered for dispatch
3. Pick one instruction for each functional unit
4. **Free RS right after dispatch**. This is different than Tomasulo’s algorithm. With a ROB the instruction is broadcast with the ROB name rather than the RS name, so the RS can be freed sooner (RS does not have to hold reg name anymore, ROB does it)

##### ROB Broadcast
1. to Reservation Station (capture)
2. to **ROB** (mark Done Bit as 1 as well)

##### ROB Commit
1. Check inst completeness (committed) starting from oldest in ROB, wait for all prev inst to have committed (**commit ptr++**) until target ROB inst entry
2. (If done bit == 1) WB to Reg. Note that this way **register writes are occurring in order.**
3. Update RAT & Reg file
4. Free the ROB entry

##### Inst Sche w ROB example
difference from Sche w/o ROB:
- **Issue**: write a new ROB entry also; RAT entry point to ROB entry, not RS entry
- **Dispatch**: free RS right after dispatch/EXE
- **Broadcast**:  write to ROB (and update done bit)
- **Commit**: new phase, write to Regs file & update RAT in program order
	-	![[isnt sche w ROB.png|600]]
	-	RAT & Regs updt on commit:
		-	![[RAT updts on commit.png|600]]
			- Commit ROB inst
			- WB result value to Regs
			- Check RAT: if this entry is not in RAT, do nothing; if in RAT, it means it is the latest value for that Reg, so update RAT to directly point to Reg file.
		- This way, **Registers are always up-to-date at every commit**, which improves exception handling.

##### Hardware Organization with the ROB
The ROB has a head, the next instruction to be issued, and a tail, the next instruction to commit. Entries in between these two are being executed.

The ROB is used to:
- Remember the program order
- Temporarily store an instruction’s result
- Serve as the name (tag) for the result

##### Branch Mispred Recovery
as shown in example, ROB controls **writing to Regs in program order**. If branch mispreds and wrong insts after it are executing, recovery process is:
- empty ROB entries after mispred & issue ptr reverse back to commit ptr (at misbranch inst)
- update relevant RAT, point them back to Regs
- empty relevant RS, ALU if still running
![[ROB in branch mispred.png|600]]

##### ROB and Exceptions
Core idea is **treat Exceptions as result for an inst**, so that actual handling of that exception is **delayed until commit**. Thus **write to reg in program order** is still reserved. This means:
- OOO inst: when exception handling is being committed at one inst, every inst entry after it is **flushed.**. (**How can those following insts rerun after flush???**): (because after exception handler done, it returns back to PC of that DIV inst, fetch->decoder does inst after DIV in order again like it never happened.)
![[ROB exception eg.png|600]]
- Phantom Exceptions: misbranch exception committing will flush phantom exceptions after it that are not handled yet. 

Commit is the **outside view of "executed"** by programmer. So programmers will always see correct inst path.

##### ROB final example
- why can Inst 5 be issued, operands captured, dispatched all at cycle 5? - Depends! 
![[rob eg.png|600]]

##### Unified Reservation Stations
combine the reservation stations for the _Adder_ and the _Multiplier_. All of the reservation stations are in one large array, so the reservation stations can be used when necessary, they do not have to wait for a specific set of RS. The RS logic will be more complicated this case.

##### ROB Superscalar
A superscalar process must be able to:
- Fetch > 1 inst/ cycle
- Decode > 1 inst / cycle
- Issue > 1 inst / cycle
- Dispatch > 1 inst / cycle
- Broadcast  > 1 inst / cycle
- Commit > 1 inst / cycle

Think of it as  a pipeline. **CPI is limited by weakest link**. For example if Decoder can decode 2 inst / cycle while others do 4 inst / cycle, overall processor CPI is limited to 2 inst / cycle.

##### Terminology Confusion
Most research papers will use: Issue, Dispatch, Commit. Processor Designers will often give different names.