![[par bfs.png|500]]

Depth of BFS search should be "diameter" of graph, or the longest distance between two nodes (i.e. the number of waves from one node to spread over to another node)

### Algorithm
pseudo code
-  l ← 0 ..... the code is level synchronous. This is the level counter set to 0
-  The frontiers referenced are also level specific (Fl)
-  l ← l + 1 .... increments the counter
-  The span (defined by the while loop) will be no larger than the diameter of the graph
-  Process level will: take the graph and the current frontier. It will produce a new frontier and update the distances (D)
![[par bfs pseudo  code.png|400]]

- using bag,putting all  together
	- run time: O(d*V*E)
![[par split algo total.png|500]]

### Data structure: Bag
bag property:
- The data is an unordered collection
- It will allow repetition
- Allow redundant insertions of the same vertex, if necessary

operations:
- traversal
- union, split

##### Pennant
Pennant is: a tree with 2k nodes and a unary root having a child. the child is the root of a complete binary tree. X is the root. Xs is the complete binary tree. So a pennant has **2^n** nodes. Essentially a binary number representation, a binary can be represented as a series of pennants. 

For example, bag of 23 nodes = 2^4 size pennant, 2^2  size pennant, 2^1 size pennant, 2^0 size pennant ($23=10111_2$). Since it is essentially a binary number, 
- it can easily do one element insertion or even two bag union like binary addition. (logn run time)
- logn time for split as well
	- essentially a binary right shift 
	- ![[bag split.png|400]] 
