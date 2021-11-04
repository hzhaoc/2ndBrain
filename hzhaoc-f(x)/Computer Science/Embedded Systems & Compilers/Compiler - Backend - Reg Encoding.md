reg field size in instruction limits number of registers for naming, the topic is how to encode registers as few bits as possible, especially when there are many regs.

# Differential Register Allocation
Use modulo difference to last register to encode current register. This way, we save bits in instruction register bits field and avoid negatives, resulting in speedup.

In some cases, you still need many bits. For example, for 8 register architecture, reg 0 -> 7 still needs 3 bits in difference. We introduce a new narrow inst: `set_last_reg(Reg num)`,  when used, diff will be 0.
![[diff encode.png|300]]

-  multi path inconsistency
	-  with two paths converge, we choose one path (maybe most taken branch) to do modulo difference and the other one  we put `set_last_reg(Reg num)`

- hardware implementation for decoding
	- Need a narrow register - to hold the last register accessed (last_reg)
	- Adders to deal with the short integers used to calculate the decoded registers. 128  registers will use 7 bits.
	- Decoding can be performed in parallel while the opcodes is being decoded.
	- We can even parallelize the decoding of the registers.

### integration into [[Compiler - Backend - Reg Alloc|Register Allocation]]
![[diff encode in reg alloc.png|500]]

##### adjacency graph
in the graph, node is a virtual reg, edge weight is frequency of adjacent reg accesses.
- a covered edge is  an edge whose modulo diff of two adjacent regs can be directly encoded without `set_last_reg(Reg num)`, vice versa.
- cost = weight of uncovered edges, or number of new `set_last_reg(Reg num)` instructions needed.

##### differential remapping
- assign regs to nodes on adjacency graph
- perform global remapping / permute reg numbers after reg alloc (postpass) is done to maximize coverage weights on graph

- a heuristic algorithm
-	initialize a reg vector
-	calculate cost from graph
-	swap a pair of regs in graph
	-	if cost reduced, do swap again
	-	if not, exit

##### differential select
How can we modify the differential select algo
1. Pop a virtual register from the stack
2. Insert it into both an interference graph and the adjacency graph
3. Recover the edges to the neighbors that have been inserted prior to this node
4. Check the interference graph to get a number of register numbers (Colors) that are not used by its neighbors. If no available register number (color), the register allocator will handle that as spill.
5. For each allowed register number, find extra cost that will be incurred if the node is assigned this register number.
6. Pick the one with the minimal cost.

The result: Amongst available colors the one that covers maximum edge weights in the adjacency graph is the one that is picked

##### Differential Coalesce
Used this algorithm to see if differential register allocation can be used.
- More registers are exposed and used → so spills are significantly reduced in stage 1 (optimal spills stage). 
- We need to tackle both move and set_last_reg instructions in stage 2 (move coalescence stage). This makes it more sensitive to the set_last_reg instructions that are being inserted.
- Integrate differential select into stage 2 to search for a solution which reduces set_last_Reg instructions as well.

##### applications
- software pipelining that increase reg pressure due to optimizations like unrolling
- selectively turn on and off diff encoding depending on reg pressure for each region.