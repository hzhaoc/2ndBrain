 instruction level parallelism
 
## RAW dependencies
in multi-inst per stage pipeline: STALL before `EXE` + FORWARD

## WAW dependencies
in multi-inst per stage pipeline: STALL before `WB` (write back)

## Remove False dependencies (WAR, WAW)
### Duplicate [[Instruction Register]] values
Write to same register with multiple values by some order. 
### Register renaming
Every time inst updates RAT from [[Instruction Register]], it renames that entry (so it maps to another physical location in Physical Register).
#### [[Instruction Register]]:
-	Architectural Reg = Reg that Programmer / Compiler uses
-	Physical Register
-	Architectural Reg maps to Physical Reg through **RAT (Register Allocation Table)**.

## Instruction level parallelism
ILP = IPC when:
-	Processor does entire inst in 1 cycle (no pipeline)
-	Processor can do any number of insts in same cycle 
-	Obey Data True Dependencies
ILP is a property of a program, not of a processor.

### ILP with structural dependencies and control dependencies
- No structural dependencies (this happens when there's limited source for hardware in same cycles, ILP is only a property of program itself)
- Assume perfect same-cycle branch prediction. So branch inst dependencies should be ignored in calculating ILP.

### ILP vs IPC
- Narrow issue in-order processor: IPC is limited usually by number of issues per cycle.
- Wide issue in-order processor: IPC is limited usually by in-order.
- Ideal is to have a wide-issue out-of-order processor.