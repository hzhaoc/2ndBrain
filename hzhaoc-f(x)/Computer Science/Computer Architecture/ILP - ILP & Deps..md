 In theory if there are no instruction dependencies & hardware can issue infinite instructions in one cycle, then ideal CPI would be 0.
 
 ILP is a property of a program, not a hardware. **ILP is only limited to true data deps.**
 
 # Dependencies
 ### Structural Dependencies
Subject to limited hardware resources such as 3-issue CPU with 2 ALU unit.
### Control Dependencies
Control dependencies are due to program, not pipeline
- Inst: **Branch/Jump**
About 20% of insts are Branch/Jump.
- Inst: **Taken insts** (actually go to jump inst) are 50% of Branch/Jump insts.
### Data Dependencies
##### RAW
- Read after write. **True dependency.** which means it has to be worried about for ILP as it can cause **hazards**.
- How to solve hazards: STALL before `EXE\ALU` + FORWARD so that dependent variable can get forwarded updated value and then do `ALU` right after `ALU` stage which the variable is dependent on.
##### WAW
- Write after write. **False dependency** or write over where a register is written from multiple values. False dependency can be removed from register renaming in compiling.
- In multi-inst per stage pipeline: STALL before `WB` (write back to register) so that the relevant register value is written back from the last variable (the dependent variable).
##### WAR
- Write after read. **False dependency** or anti dependency. False dependency can be removed from register renaming in compiling.
- Personally think no need to be considered here for ILP (see below Reg Renaming example to remove WAW).

### Remove false dependencies (WAR, WAW)
##### Approach 1: Duplicate [[Storage Hierarchy#Register|register]] values
Write to same register with multiple values by some order. Needs hardware support.

##### Approach 2: Register renaming
There are two types of registers: 
1. Architectural Reg. that programmer/compiler uses.
2. Physical Reg. where values are stored like 1. 

Compiler rewrites architectural regs to physical regs fed to processors, this scheme is called "**Register Renaming**". Every time program updates **RAT (Register Allocation Table)** for regs mapping, and it renames reg entry (so it maps to another physical location in Physical Register).

A RAT is a table that maps virtual registers to physical registers. For example, for an instruction `MUL R2, R2, R2`, `R2` is mapped to `P2`, then writes result to a new physical register `P7`, and this is updated in RAT.

**Here is a register renaming example**:

The program on the left part is architectural insts; the program on the right part is physical insts compiled from left part. As the program is running, RAT will see the change of the register renaming process. registered fetched from architectural registers will be renamed and written back to new physical registers. In this way, **false dependency WAW on the 2nd and 5th insts (from top to bottom in the picture) is removed. (when there's a R4 reg needs to be read later on (see the bottom of the pic), it will use P21 which is R4 from the 5th inst in the program)**. When you calculate an ILP of a program, just ignore false dependencies and only focus on RAW.

On a side note, I personally think although reg renaming removes WAW & WAR, WAR does not need to be considered for potential hazards because the register is read in ALU or MEM stage (?), and after that instruction, the same register is being written in the final WB stage. This process does not create conflicts for this register to be read or written in later instructions.

![[reg_renaming_eg.png]]

### Instruction Level Parallelism
**ILP is a property of a program, not of a processor.**. Think of a program ILP as what IPC a processor can achieve assuming it can do infinite insts in same cycle, an entire inst is done in one cycle (pipelines are not considered here!), and the only data dependencies are true dependency / RAW. 

ILP = IPC when:
-	Processor does entire inst in 1 cycle
-	Processor can do infinite insts in same cycle
-	Processor does perfect branch prediction (or it is not considered)
-	Processor has unlimited resources so no structural dependencies.
-	Processor can issue out of order insts.
-	**Only True Data Dependencies are considered**

### ILP w/ structural & control dependencies
- A program's ILP property assumes **no structural dependencies** (this happens when there's limited source for hardware in same cycles)
- Assume perfect same-cycle branch prediction. So branch inst dependencies should be ignored in calculating ILP.
Below example illustrates how control dependencies are ignored in calculating ILP.
![[ILP w control dependency.png]]

### ILP vs IPC
- Narrow issue in-order processor: IPC is limited usually by number of issues per cycle.
- Wide issue in-order processor: IPC is limited usually by in-order.
- **Ideal is to have a wide-issue out-of-order processor, where false deps are removed, and insts will be reordered (due to out-of-order)**.