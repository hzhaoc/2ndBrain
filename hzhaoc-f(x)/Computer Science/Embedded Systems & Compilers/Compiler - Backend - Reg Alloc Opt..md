##### Cache Energy Consumption
Load/stores that go to cache generate many activities (lookups, tag computation, data transfer, etc.), which consumes energy. **Feedback directed post-pass register reallocation** can be used to after normal register allocation is done, **to reduce load/stores with cache**. 
- **The goal here is to reduce energy consumption by reducing load/stores, not to reduce run time since load/stores are pipelined.**

Traditionally, physical registers are directly allocated on demand and memory store/loads occur when there are spills. In modern processors, infinite symbolic/virtual registers are mapped to finite physical registers. 

##### Postpass Optimization
After normal heuristic algorithm of construction of code, there are dead or unused registers  especially when number of available registers are low like 16 or 8. 
- dead register: a register that contains a value not used anymore
	- solution is usually load a new value
- unused register: a register that contains a value for a long live range but will not be used in near blocks. We can use splitting here but it may be too costly.
	- solution is usually store the value, load a new value, then restore previous value when it is used later

The optimization is 
1.  first to identify **hot regions** of code (usually in loops, about 0.3 hot and 0.7 cold codes empirically). 
	-  can use a threshold (like avg exe freq of all basic blocks) to check if a region dynamic execution freq is above this.  The  dynamic frequency can be found during profiling.
	-  merge all adjacent hot regions **so disjoint hot regions by cold regions register re-alloc can be done independently.**
2.  redo the reg alloc on the hot regions to reduce dynamic cache loads/stores
	-  identify dead/unused regs
	-  identify spills
	-  weighted bipartite graph matching
		-  one party: spilled variables with block number
		-  another party: dead/unused variables with block number
		-  edge: if a variable and a register is matched, create an edge whose weight is determined by the number of dynamic spill  loads/stores associated with the edge.
		-  matching goal here is to optimize total edge benefit/weights
	-  compensation code cost analysis
		-  in different blocks, choose edges on same variable-register.
		-  combine such edges across adjacent blocks to avoid compensation code as much as possible. 
		-  after computing such largest compensation code free region,  find  compensation costs at boundaries:
			-  load in cur region
			-  or store in cur region
			-  or load in pre region
			-  or store in next region
	-  unused reg alloc
		-  identify unused register region: merge adjacent blocks to find largest unused region for  that unused register. 
		-  regions can overlap for different unused regs
			-  find maximum benefit region
			-  alloc those unused regs in this region
			-  find next highest beneficial unused reg region, repeat.
		-  Compensation Cost Analysis:
			-  store original value back to memory
			-  load variable into unused register
			-  store variable back to memory
			-  load original value to unused region

##### some notes...
even with a perfect reg allocator, there may still be dead or unused regs needed for postpass realloc due to gaps??
