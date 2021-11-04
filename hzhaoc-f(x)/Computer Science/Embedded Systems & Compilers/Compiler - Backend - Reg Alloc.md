This part of the course will focus on backend cod regeneration.
- Backend: generation of assembly instructions from IR
	- Then: selecting instructions
	- **register allocation** on them
	- instruction scheduling
- Preparing IR for Efficient Code Generation (register allocation)

First step of **Code Generation**:
- Convert IR into [[Compiler - Intermediary - CFG|CFG]]
- Perform data flow analysis: [[Compiler - Backend - Liveness|liveness analysis]]
- Gather Live variables Information: perform **register allocation**

Register allocation: there are few registers are available: 32 float registers, 32 integer registers.  some registers have special purposes 
- integer reg
- float reg
- doubleword registers (odd/even pairs)
- branch and predicate registers
- stack pointer including the _activation record (AR)_ (all the local variables, return address, etc. for function calls. 
- R0 - holds the program, this register is initialized to the address of the program
- string manipulation - registers for implicit uses.

In this lesson we will be focusing on: **general purpose registers for holding integers and floats**.

##### Goal
maximize duration of each register value. Probably the optimization with the **most performance impact**.

##### Definitions
- **gen**. (generated) variable is newly defined
- **kill**. old value is no longer accessible.
- **def**. on left hand side (a = 5) a is on the LHS
- **use**. on the right hand side (a = b + c) b and c are being used
- **live**. variable will be used again (before it is overwritten) (a = 10 , ...... , c = a + b :: ‘a’ is live because it is used)
- **dead**. variable will never be used again and the variable will be overwritten before the next use

### register allocation process
##### overview
-  draw an interference graph where register nodes whose live range overlaps are connected with edges. 
-  color nodes. connected nodes must belong to different colors.
-  **then the maximum number of registers needed are the number of colors in the graph.**

Usually, there are more variables than registers, so the **decision is which value(s) are kicked out of which registers.**

##### formal definition
1. Determine live ranges for each value (web)
2. Determine overlapping ranges (interference)
3. Compute the benefit of keeping each web in a register (spill cost). **Spill cost** = cost of keeping "spilled" values in memory when registers are full.
4. **decide which webs get a register (allocation). (many algorithms for this)**
5. Split webs if needed (spilling and splitting)
6. **Assign hard registers to webs (assignment coloring)**
7. Generate the code - including spills (code gen). Spill = a value needs to be removed from a register, but it is still live (store to memory)

##### Web
Web: a way to extend liveness across basic blocks. It start at definition, end at end of use

def-use (DU) chains
- connects definition to all reachable uses
- conditions for putting defs and uses into the same web
- definition and all reachable uses must be part of the same web
- all defs that reach the same use must be in the same web

![[webs register allocation.png|500]]

##### Interference
Two webs interfere if their live ranges overlap (have a non-empty intersection). 
- If two webs interfere, values must be stored in different registers or memory locations. 
- If two webs do NOT interfere, they can store values in the same register or memory location.

With this interference graph, we do register allocation.
- two nodes with edge connected must have different colors
- maximum registers needed are number of colors in the graph
- the problem is [[NP Complete]]. But good heuristics exist.

##### Graph Coloring Heuristics
To find the minimum number of colors during compile time could take an incredibly long periodof time. So most graph coloring heuristics seek an **almost** minimal set instead of the minimum set.
- if degree < N (degree of a node = # of edges it has). 
- A Node can always be colored. As long as the number of neighbors are less than N, the node can always be colored. 
- After coloring the rest of the nodes, you’ll have at least one color left to color the current node. 
- If degree >= N it **may or may not** colorable with N colors.

##### **Graph Coloring Heuristics** (Brigg's Algorithm)
- Remove nodes that have degree < N (colorable nodes)
	- push the removed nodes onto the stack
- When all the remaining nodes have a degree >= N
	- Find the node with the least spill cost and push it onto the stack
	- What we are doing is ordering the nodes on the stack in the order of their spill cost. The top of the stack will have the highest spill cost, the bottom of the stack will have the least spill cost. The nodes with the highest spill costs will get registers. 

When all the list of nodes is empty, it is time to start coloring. 
- Pop a node from the top of the stack (highest spill cost). 
- Assign it a color that is different from its connected nodes (since degree < N, a color should exist). 
- If there is not a color available, then there will be a spill. This way, the spilled cost will be from node whose degree > available colors (registers) but not too high. 

##### When Coloring Fails
What are the options:
1. pick a web and allocate the value in memory. All the definitions go to memory, all uses come from memory. 
2. Split the web into multiple webs. In either case, will retry the coloring. For splitting,  Which web to choose?
	-  one with interference degree >= N
	-  one with minimal spill cost (cost of placing value in memory rather than in register.) 

Ideal spill cost: dynamic cost of extra load and store instructions. Can’t expect to compute this.  
- Don’t know which way branches resolve. 
- Don’t know how many times loops execute. 
- Actual cost may be different for different executions. 

Solution: Use static approximation profiling can give instruction execution frequencies or use heuristics based on structure of control flow graph. The second technique is usually used in practice. Computing spill costs using heuristics based on structure of control flow graph. 

Goal: give priority to values used in loops. 
- Assume loops execute 8 to 10 times. 
- Spill cost = sum over all def sites: cost of a store instruction times 10 to the loop nesting depth power, plus sum over all use sites: cost of a load instruction times 10 to the loop nesting depth power. Then choose the web with the lowest spill cos

##### Splitting the Web
Split a web into multiple webs so that there will be less interference in the interference graph making it N-colorable. **The web that should be split - highest interference and lowest spill cost.** 
- Cost: After splitting spill the value to memory and load it back at the points where the web is split. proportional to the number of time the split edge has to be crossed dynamically. Estimated by its loop nesting
- Benefit: less interference, more chance to be N-colorable so less spill cost from this. 

##### Splitting Heuristic
- Identify a program point where the graph is not R-colorable (point where the number of webs > N).
- Pick a web that is not used for the largest enclosing block around that point of the program (little spill cost). Split the web at the corresponding edge. 
- Redo the interference graph. Try to recolor the graph

Greedy Heuristic: pick the live-range with the highest benefit of cost ratio to spill

##### Further Optimizations
- **register coalescing**
	- Find register copy instructions sj = si (register to register copying)
	- Remove these by combining their webs into one web: if sj and si do not interfere, combine their webs
		- Pros: reduce the number of instructions
		- Cons: may increase the degree of the combined node - a colorable graph may become non-colorable
- **register targeting(pre-coloring)**
	- Some variables need to be in special register at a given time
		- first 4 arguments to a function
		- return value
	- Pre-color those webs and bind them to the correct register
	- Will eliminate unnecessary copy instructions
- **presplitting of webs**
	- Some live ranges have very large dead regions. This is a large region where the variable is unused.
	- Break up the live ranges
		- need to pay a small cost in spilling
		- the graph will be very easy to color
		- Can find strategic locations to break up
			- at a call site (because you need to spill anyway)
			- around a large loop nest (reserve register for values used in the loop)
- **interprocedural register allocation**
	- Saving and restoring registers across procedure boundaries is expensive
		- especially for programs with many small functions
	- Calling convention is too general and inefficient 
	- Customize calling convention per function by doing interprocedural register allocation
		- You may need to create a clone version of the function. A clone version is only effective at the call site, it has a specialized register allocation