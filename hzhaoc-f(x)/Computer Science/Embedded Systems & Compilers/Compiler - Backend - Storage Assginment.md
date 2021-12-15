Manage sequence of accesses to efficiently use address registers in instruction sequence.

### Simple Offset Assignment (SOA)
###### assumptions
- every object address is size of one word
- a single address register is used to address all variables
- one-to-one mapping of variable-address
- basic block has fixed evaluation order or schedule.

##### Auto Increment Mode
Get the operand and increment in same instruction. It reduces code size and improve efficiency. So best to utilize this and maximize auto increments in instruction sequence.

##### Access Sequence
Sequence in which the memory locations are accessed. For example, 
```
z = x + y
```
is in the sequence of `xyz`

##### Access Graph
- **Nodes** are unique variables. **Edges** are adjacent variables in sequence accesses whose weight are number of adjacent accesses.
- **Weight of the Graph** is sum of all edge weights/cost.
- **Path Cover**: A sub-Graph or a subset of paths such that each node belongs to **exactly** a path in the graph. It may include isolated node or path of 0 length.
- **Maximum Weighted Path Cover (MWPC)** is a path cover whose weight is maximal, and therefore its cost (original graph weights - MWPC weights) is minimal.

### General Offset Assignment (GOA)
- k address registers
- given access sequence L, set of variables V, number of address registers K
- find a partition of V, where m <= K
- such that total cost of the optimal SOA of each sub-sequence plus setup cost for using the m registers is minimal.

###### assumptions
- fixed setup cost of each address register
- each address register is used for one disjoint subset of variables

##### a heuristic algorithm for GOA
![[GOA heuristics.png|400]]
key is 
- line 8: graph partition into two parts by selecting a subgroup of variables 
- line 11-12: SOA algorithm

##### GOA with Relax Fixed Evaluation Order Assumption
Use algebraic properties:
- commutativity
- associativity

to rearrange sequence of variables in instruction code in order to possibly find a better MWPC and thus reduce instruction cost.

for example, 
```
a = b + c + d + e
```
of sequence `bcdea`

can be rearranged to 
```
a = c + b + (d + e)
```
of sequence `decba`

##### Least Cost Access Sequence
The rearranged Access Sequence of all that has the minimal sequence access cost by solving SOA.

This means: 
- Do algebraic transformations (focus on reducing edges in graph)
- Find corresponding MWPC and cost. If cost is less than the SAO cost, try another transforming.
- We are looking for the least cost access sequence (LCAS)

### Variable Coalescence and Separation
Now we look at variable Coalescence. Variables in the memory can be coalesced (put in the same memory location)
- When the **webs** do not overlap or they do not interfere with each other
- So we must make sure the **live ranges** of the two variables do not overlap
- This will make it easier to make a better layout.

**Issues on Applying Coalescence** 
- Coalescence is not a new technique. But now we are coalescing disjointed webs to the same location. 
- Maximal coalescence may not lead to the best storage assignment. In fact it may worsen it.
	- This happens because coalescence increases the number of neighbors for coalesced nodes.
	- Only two neighbors are allowed for each node on the path cover. Increasing the degree of the nodes, MWPC must work harder to find a node pair. 

Coalescing is not the best for generating the best access sequence.

# Summary
![[SOA framework.png|500]]

**Pre-Iteration Rules**
If we apply pre-iteration rules before the coalescence iteration loop, the profitability is always guaranteed. 
- Rule 1: coalesce all degree 0 nodes with any other node. Doing so will not affect the SOA cost. 
- Rule 2: coalesce all degree-1 nodes with it neighbor. If its edge is already on the PC, the SOA cost is not affected. Otherwise we reduce the SOA cost by the weight of this edge. 
- Rule 3: coalesce all degree-2 nodes with the neighbor having a higher weight edge connected to it.

![[SOA main algo.png|550]]
