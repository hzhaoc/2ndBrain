 # Instruction Level Parallelism
 
## RAW dependencies
in multi-inst per stage pipeline: STALL before `EXE` + FORWARD

## WAW dependencies
in multi-inst per stage pipeline: STALL before `WB` (write back)

## Remove False dependencies (WAR, WAW)
- ### Duplicate [[Instruction Register]] values
Write to same register with multiple values by some order. Needs hardware support.
- ### Register renaming
	There are two types of registers: 1. Architectural Reg. that programmer/compiler uses like Add. 2. Physical Reg. where values are stored like 1. 

	Register Renaming rewrites programs to use physical registers. Every time inst updates RAT (Register Allocation Table) from [[Instruction Register]], and it renames that entry (so it maps to another physical location in Physical Register).

	A RAT is a table that maps virtual registers to physical registers. For example, for an instruction `MUL R2, R2, R2`, `R2` is mapped to `P2`, then writes result to a new physical register `P7`, and this is updated in RAT.

	ILP = IPC when:
	-	Processor does entire inst in 1 cycle (no pipeline)
	-	Processor can do any number of insts in same cycle 
	-	Obey Data True Dependencies
	**ILP is a property of a program, not of a processor.**

## ILP with structural/control dependencies
- No structural dependencies (this happens when there's limited source for hardware in same cycles,** ILP is only a property of program itself**)
- Assume perfect same-cycle branch prediction. So branch inst dependencies should be ignored in calculating ILP.

## ILP vs IPC
- Narrow issue in-order processor: IPC is limited usually by number of issues per cycle.
- Wide issue in-order processor: IPC is limited usually by in-order.
- Ideal is to have a wide-issue out-of-order processor.