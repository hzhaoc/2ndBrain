Memory have different banks upon which stores and loads can be done in parallel. Maximally merge loads and stores into parallel loads or stores which execute concurrently and process the operands accessing different memory banks.

### approach 1
a integer linear programming problem...

### approach 2: graph problem
- each load/store is a node
- edge is 1: can be merged, 0: otherwise.
- pick maximum number of edges that are disjoint to be merged

##### algorithm
- Identify the movable boundary problem (identify which of the loads can be merged together)
- Loads are in the program at code generation, but loads can be moved to take advantage of the parallelism.
- So the first step is to determine which loads and stores can be moved. This is called **Motion Schedule graph (MSG)**. There are two approaches to solve it heuristically. 
- Second step: **merge with instruction duplication and variable duplication. This means that we move the load/store instructions together, then we need to make sure the variables are in different banks.** We may need to use variable duplication - if one instruction has a variable in say, bank X and the other also has a variable in bank X, we will copy one of the variables to bank Y.
	- or, Rematerialization: recomputing a value and storing it in another bank. For example, `a=b+c`, a is stored in bank X, but we want it in bank Y for parallelization, in addition to copying it from X to Y, we can alternatively, recompute `b+c` if b and c access can be parallelized, and store result to Y.
- Sometimes the variables will be merged across basic blocks.

##### Movable Boundary Problem
trying to move load/stores within Motion Range to increase parallelism. 
- Motion Range: instruction range within which a load/stores can be moved. For example, a load's range is typically between a previous store, and next use. 
- Since a load/store's motion boundary can also be a load/store, the motion co-move and is not fixed. But we can use a Pseudo fixed boundary approach to deal with it to try maximizing motion ranges for all load/stores to create parallelism opportunities. 
	- for store: move as early as possible
	- for store: move as late as possible.

##### Motion Schedule graph
![[Motion Schedule Graph.png|500]]

![[parallel LD & ST overview.png|500]]
**Cross Basic Block Merge **
How do we carry the load/store replication across basic blocks. 
- To guarantee profitability: move to where the reference is live. If the reference is not live, all we do is increase register pressure causing more spills 
- Move the stores using the extended basic blocks.
- Move the loads on reverse Extended basic blocks
- Make sure: if moving load/stores in basic blocks that we are able to combine them with something else. So make sure it can be combined if pushed to at least one of the live predecessors/successors.
![[e.g. cross basic block merge.png]]

**Variable Duplication**.
![[e.g. variable duplication.png]]

**Local Conflict Elimination**
A conflict may occur because we are putting load/stores into the live ranges of other variables. The Register allocator may assign the same register to neighboring ranges, which leads to register conflicts. ISA restrictions may need particular register but not be available at the program point. **Rematerialization** to free a register and reconstruct it after the merge to make the register available.