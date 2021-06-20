You already know:
- Control dependencies are eliminated using Branch Prediction
- False dependencies are eliminated using Register Renaming
- Instruction orders are broken using Tomasulo-like scheduling (**for non-Mem Regs**)

This topic will tell you a method for handling mem (RAW/store-then-load) deps: the **Load-Store Queue (LSQ)** which can be either in-order or out-of-order with recovery process

### Load Store Queue
LSQ helps some loads (insts) get store values with same addr directly from this queue without going to mem. 

Write to Mem occur at [[ILP - Out-of-Order EXE w Reorder Buffer#ROB Commit|Commit]]. The LSQ has following fields:
- A bit indicating load or store
- mem address of the load or store
- data to be stored (or load?) in mem
- a bit indicating completion

Loads & Stores insts are placed in LSQ **by program order.** 

##### Store-to-Load Forwarding

When a load is put in LSQ, it searches all prev inst addr. If there's a match, the value in that entry is forwarded to this load's value. If not match, go to mem. 

When a store does not have its address when a load is checking the queue, options are:
- wait for the store to get address. Slow.
- **In-Order**. wait for all prev stores to get addresses. 
- **Go to mem directly**. when prev store gets its addr, it checks all loads after it, if it finds same addr for a load that already went to mem for value, it requests a recovery process for that load because the load inst has violated RAW mem deps. This is used by most modern processors (2021) because it results in relatively best performance. (low probability for same addr between a load & store that violates RAW deps)

Below example shows load-to-store forwarding & directly-go-to-mem load when there's prev no-addr store and following RAW solution (later same-addr store checks all loads and requests recovery)
![[load-store-queue for mem deps.png|650]]

##### In-Order Load-Store EXE
Do load and stores in-order. **A load cannot execute until all prev stores have their addr known.** After all prev stores have their addr, the load will check addr match. If so, forward in LSQ. If not, go to mem. Note all other insts are still EXE OOO.

Not a high-performance solution.

##### Out-of-Order Load-Store EXE
Remember when a load is in LSQ and sees prev store with no addr, one most used option is go to mem directly. And if later on the prev store gets addr the same as this following load, it checks, sees it, and requests a recovery. The recover flush this load (& all insts after it probably for deps) and redo. Thus OOO. 

### LSQ, ROB, RS review
When issue load/store:
- a ROB entry
- **a LSQ entry**

When issue non-load/store:
- a ROB entry
- **a RS entry**

Execute load/store
- compute addr
- produce value
- **(load) write to reg**

Commit load/store
- free ROB & LSQ entry
- **(store) write to mem**



