### Control Flow liveness analysis
A variable is considered **live** before a instruction or basic block when it is available/computed before it, and live after an instruction or block when it is computed after the instruction or block and needed later.
$$in[I]\ =\ (out[I]\ -\ def[I])\ U\ use[I]$$

![[liveness variable.png|500]]

Use this equation to solve liveness variables at each program checkpoint in a **backward** manner. With this liveness information, we can perform **[[Compiler - Backend - Reg Alloc|Register Allocation]]**.