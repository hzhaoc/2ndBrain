This topic discusses some of the techniques used by compilers to achieve greater ILP. Improving **[[ILP - Out-of-Order EXE|inst sche]]** and reducing **inst #** are the basic goals of compiler ILP.

##### Tree Height Reduction
Tree height refers to the dependence chains in a list of instructions. Tree height reduction is regrouping the calculations in an instruction list to reduce the dependencies. **This method only works for calculations that are associative.** See below ADD example:
![[compiler ilp - tree height reduction.png|600]]

## Making Independent Instructions Easier to Find
- inst sche
- func inlining
- loop unrolling
##### Instruction Scheduling
When there is a dependency between instructions, there is often a need for the processor to stall between instructions. A stall can be replaced with an independent instruction, as long as the program produces the correct result. **Sometimes the correct result requires modifying additional instructions.** So compiler tries to reorder instructions to reduce STALL latency. 

Modifications include:
- **addr offset change** (happens when inst moves relative to an addr fetch)
- **dest reg change** (happens when an inst move causes a reg to be re-written earlier in the program than expected)

For one example, notice ADD1 does not have deps, and can be moved to the first STALL to hide it. Then when store to R1, simply decrement address.
![[compiler inst sche.png|600]]
For another example, see below, rename R1 to R10 in insts between 4th and 6th. It doesn't affect the program correctness. Then insts can be reordered to hide LW (load word) latency.
![[compiler inst sche 2.png|600]]
##### Inst Sche in If-Conversion
1. Do [[ILP - Ctrl Deps. Branch Predicate]] to avoid branch prediction
2. Now you have stable inst flow, do inst sche as said above

##### Loop Unrolling + Inst Sche.
Loop unrolling **creates a loop with fewer iterations by having each iteration do the work of two or more iterations**. This will reduce the number of branches that need to be executed and it increases the number of instructions that can be considered during the instruction scheduling. See below example:
![[compiler loop unrolling.png|600]]
- Benefits:
	- **total dynamic # goes down** (10->8 per loop see above eg)
	- **CPI down too** (with unrolled, compiler can also does inst reordering to reduce CPI more)
- Downside:
	- Code Bloat (too many codes expanded)
	- not good when iter # unknown
	- not good when iter # not multiple of unrolling times
- Note
	- Cannot unroll loop all like if-conversion due to too many predicates.
	- Cannot unroll all due to code bloat usually

##### Function Inlining
Make function call -> return part of the inst sequence instead of a call.
- Benefits:
	- eliminates inst of call func. 
		- inst # goes down.
	- eliminates inst of func params copying. 
		- inst # goes down.
	- eliminates inst of func return. 
		- inst # goes down.
	- reduces even inst of preparing for func params. 
		- inst # goes down.
	- because func codes are inline, can do reorder (inst sche.). 
		- CPI goes down.
- Downside:
	- code bloat (the smaller the func, the more above benefits of inlining)

##### Other Compiler ILP techniques
- **Software Pipelining**:
	- to optimize loops for OOO, make insts independent in one iter and instead interdependent on neighbor iterations.
- **Trace Scheduling**
	- in if-conversion, schedule insts for most common path, for the other path, do fix.