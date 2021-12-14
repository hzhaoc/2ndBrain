### The Graph Partitioning Problem
Look at the problem from a different angle: 

Let’s multiply a sparse matrix ‘A’ by a vector ‘X’. Recall the duality between matrices and graphs: 
- Rows and columns are vertices. 
- The non-zeros are edges.

One way to do a BFS is to do a computation that looks like a linear algebra problem: 
- y ← A . x (A multiplied by x) 

To distribute the work by rows: 
- Assign rows to processes. This is equivalent to partitioning the graph. 
- When you partition the matrix, this implies that you are also partitioning the vectors x and y. This occurs because there is a one-to-one mapping of vector entries to graph vertices. 
- Work = O(non-zero) = the work is proportional to the number of non-zeros. (If n is the number of non-zeros in the row, then the depth of the computation is the depth of the sum, which is O(log n), and the work is the sum of the work across the elements, which is O(n).)

**How to choose partitions:** (NP-Complete)
- Goal 1: Divide up the rows to balance the number of non-zeros per partition. 
- Goal 2: Minimize the communication volume by reducing the edge cuts.

![[network graph partition.png]]

### A Simple Heuristic - Bisection
(based on divide and conquer) Give a graph G, divide it into P partitions.
- step 1: Divide the graph into two partitions
- step 2: Divide each half into two
- step 3: Continue to divide each partition into half until P partitions are reached This works, but how do we get two way partitions?

##### Planar Graphs
> In graph theory, a planar graph is a graph that can be embedded in the plane, i.e., it can be drawn on the plane in such a way that its edges intersect only at their endpoints. In other words, it can be drawn in such a way that no edges cross each other.

> Planar Graph Theorem:
> ![[planar graph theorem.png]]

> BFS on bisection
> 1. Pick any vertex as a starting point 
> 2. Run a level synchronous BFS from this vertex 
> 3. You will notice that every level serves as a separator. 
> 4. Because of this, you can stop when you have visited about half of the vertices. 
> 5. Assign all visited vertices to one partition and all unvisited vertices to the other partition.

##### Kernighan-Lin
> running time: $O(|V|d)$ V is vertexes, d is max in-degree

for any partitioned graph V1, V2, denote 
- Cost(V1, V2) = number of crossing edges.

for any node a in V1, any node b in V2, denote
- E(a) = number of nodes external to V1 (nodes that cross B)
- I(a) = internal nodes
- same for b.

![[graph partition - kernighan lin.png|500]] ![[kernighan lin part 1.png|500]] ![[kernighan lin part 2.png|500]]

### another partitioning strategy: graph coarsening
based on divide and conquer

goal of graph coarsening: take a graph, coarsen it so it looks similar to the original graph but with fewer nodes. Do this until you achieve a graph that is small enough to partition easily.

How to Coarsen a Graph: 
1. identify one subset of the vertices to collapse or merge
2. Replace the subset with a single super vertex. 
3. Assign a weight to the super vertex that is equal to the number of vertices it replaced. 
4. Assign a weight to the edges.

> example
> ![[graph corase eg.png]]

- **maximal matching**
Do coarsen a graph effectively, a scheme is necessary to determine which vertices to combine.. One idea of coarsening : compute a matching

> Matching: a matching of a graph G = (V,E) is a subset of E^ ⊆ E of with no common endpoints.

##### complete algo
- at each coarse stage
	- pick any vertex
	- do maximal matching iteratively, (choose one with highest edge weight)
- at some coarse stage when you think it is okay to stop and partition the graph, using for example, Kernighan-Lin algo.
- now iteratively, get the partition cut back to finer graph, and finally to the original

> **Projected Separator**: the vertices and edges that will be combined in the next level of the graph. There can be a situation where the next level graph maps ambiguously to the previous level.

##### a specific partitioning spectral partitioning
Consider an unweighted directed graph, G. When represented by an incidence matrix, each row is an edge and each column is a vertex. Put a 1 at the source, and a -1 at the destination.

Graph Laplacian $$L(G)=C^TC=D-W$$
- diagonals are degrees
- off-diagonals indicate presence of an edge

> - L(G) is symmetric
> - L(G) has real-valued, non-negative eigenvalues and real-valued, orthogonal eigenvectors.
> - G has k connected components **if and only** if k’s smallest eigenvalues are identical to 0.
> - The number of cut edges in a partition is: $\frac{1}{4} x^T L(G)x$. So if you want to minimize edge cuts, minimize the product.

The Algorithm for Spectral Partitioning 
1. Create L(G) 
2. Compute the second smallest eigenpair of L(G)
3. Determine the partition using the signs of the eigenpair