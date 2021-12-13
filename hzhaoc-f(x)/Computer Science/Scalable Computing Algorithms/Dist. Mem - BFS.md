- adjacency matrix

##### Matrix-based BFS 
Now translate the BFS algorithm into the language of Matrices. Is there an edge from the frontier to $i$? If there is, the distance should be updated. If there is an edge from j → i, then the adjacency matrix should have a ‘1’ (or true) at $a_{ji}$ . Consider the graph as a matrix A and the frontier as a boolean vector ‘f’. To determine if there is an edge from i to the frontier, there needs to be an i at the corresponding vertices. To record these edges, mark them in a boolean vector called ‘u’ (for update).

![[dist bfs.png]]

1-D Distributed BFS
The matrix gives you an easy way for distributing the BFS. 

To do this: Divide the number of columns into equal sections for each processor. The column partitioning corresponds to the partitioning of the vertices. The update vector will be partitioned to each process, but the frontier vector will need to be replicated on each process. With each update, you will need to replicate the frontier again. Use **all-to-all**.

The Distributed 1-D Algorithm 
1. partition columns of A and entries of u. 
2. Compute $u ← A^T f$ 
3. Locally update the local distances 
4. Identify local vertices of the next frontier 
5. To an all-to-all exchange of the frontier. 
 
The all-to-all is the only communication step, what is the cost? The 1-D costs scale linearly. What is the cost when it is 2-D? $\sqrt{p}$ (p is the number of processors).