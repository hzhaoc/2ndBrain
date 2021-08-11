# Principal
See also [[Computer Science/Algorithm/Principals#Dynamic Programming]]
-   Identify a problem's **optimal structure** in relation to its **optimal substructures**.
-   Use this relation to breakdown problem and build optimal structure bottom-up

# problem: max weight of independent set in graph
-   Denote Gi = first ith vertices of graph G, A\[i\] = value of max Independent Set of Gi
-   Initialize A\[0\] = 0, A\[1\] = w1
-   Loop i = 2, 3, ..., n:

> A\[i\] = max{a\[i-1\], a\[i-2\] + wi

### code implementation
```python
def MaxWeightIS(weights):
	"""max weight of independant sets from vertices (0-indexed array of vertice weights)"""
	A = dict()
	A[0], A[1] = 0, weights[0]
	for i in range(2, len(weights) + 1):
		A[i] = max([A[i-1], A[i-2] + weights[i-1]])  # A[i] = the value of max-weight of first ith vertices
	i = len(weights)
	w = dict(zip(range(1, len(weights)+1), [0]*len(weights)))  # w[i] = 1 or 0 indicates if ith vertice is in MWIS
	while i >= 2:
		if A[i-1] >= A[i-2] + weights[i-1]:  # wi not in MWIS
			i -= 1
		else:  # wi in MWIS
			w[i] = 1
			i -= 2
	w[1] = 1 if not w[2] else 0
	return w, A
```

# problem: knapsack problem
### code
```python
def Knapsack(vertices, capacity):
	"""Knapsack problem, vertices: array of (weight, size), 0-indexed"""
	A = [[0 for x in range(capacity+1)] for i in range(len(vertices)+1)]  # A[i][j] represents max weights/values for first ith vertices with capacity = j
	for i in range(1, len(vertices)+1):
		for s in range(capacity+1):
			A[i][s] = _knapsack(A, i, s, vertices)
	return A[len(vertices)][capacity]


def _knapsack(A, i, x, vertices):
	wi, si = vertices[i-1]  # weight, size of ith vertice (1-indexed)
	return max([A[i-1][x], A[i-1][x-si] + wi]) if x-si >= 0 else A[i-1][x]
	
	
def Knapsack_r(vertices, capacity, i):
	"""Knapsack problem, recursive version"""
	if i < 0:
		return 0
	w, s = vertices[i]
	if capacity < s:
		return Knapsack_r(vertices, capacity, i-1)
	else:
		return max(Knapsack_r(vertices, capacity - s, i-1) + w, Knapsack_r(vertices, capacity, i-1))
		
def Knapsack_fast(vertices, capacity):
	"""Knapsack problem, vertices: array of (weight, size), 0-indexed, minimum space storage"""
	A, pre_A = [0 for x in range(capacity+1)], [0 for x in range(capacity+1)]
	for i in range(1, len(vertices)+1):
		wi, si = vertices[i-1]
		print(i)
		for s in range(capacity+1):
			A[s] = pre_A[s] if s-si < 0 else max([pre_A[s], pre_A[s-si] + wi])
		pre_A = [x for x in A]
	return A[capacity]
```

# problem: Sequence alignment
to add

# problem: Optimal Binary Search Tree
See [[Optimal Binary Search Tree]].
- Time Complexity: $O(n^3)$
- Space Complexity: $O(n^2)$

# problem: shortest paths
### Bellman Ford
Either compute a shortest cycle-free path $s-v$ or output a negative cycle, for all paths starting from $s$
##### Pseudo code & analysis
- Let $L_{i,v}$ = minimum length of a $s-v$ path with edge number $n\leq{i}$. $l_{i, j}$ = edge length of $e(i, j)$ Cycles allowed. And $+ \infty$ if not such path exists
	- For $i = 1, 2, ..., n-1$: ($n$ if one (**only one!**) negative cycle existence needs to be checked) 
		- For $v = 1, 2, ..., n$:
			- $$L_{i,v}=min\left\{ \begin{matrix} L_{\left( i - 1 \right),\ v} \\ \min_{(w,v) \in E}\left\{ L_{\left( i - 1 \right),w} + l_{w,v} \right\} \\  \end{matrix} \right.\ $$
			- meanwhile, keep track of Predecessor pointers $B[i, v]$ = 2nd-last vertex in the shortest path. this will track shortest paths. note that $B[0, v] = null$.
			- if $L_{i, v}=L_{i-1, v}$ ($v$ is target vertex). This means optimal path is already found for path $s-v$. Can exit early. 
			- **Why the equation stands? Because subpath of a shortest path is in itself a shortest path**
			- **With negative cycles in graph: use DFS to check for a cycle of predecessor pointers at every iteration**.

> Why only one more iteration is sufficient to **one** capture negative cycles in shortest path? 
> - If there's **1** negative-cycle in shortest s-v, one of the vertex in the path Must be visited Twice, number of edges for the budget will increase by one. n-1 => n.
> - Extension: I think **K** additional iterations on top of original 0 -> n-1 will be able to capture K negative cycles in the shortest path s-v, since one negative cycle makes one vertex visited one more time, increasing edge number budget by 1.

- Time Complexity is $O(mn)$ without negative edges.

> Why it is not the intuitive answer $O(n^2)$?
> total work is $O(n*\sum_{v\in{V}}{\text{in-degree}(v)})$ = $O(n*m)$

- Space Complexity: $O(n^2)$
	- Space optimization: 
		- only need $A[i-1, v]$ to compute $A[i, v]$ for any $v$ in vertexes. $O(n)$
		- still need $O(n^2)$ for $B[i, v]$ **?**
- Modifications toward a routing protocol: 
	- Examples: RIP, RIP2.
	- Switch from source-driven to destination-driven.
		- reverse algorithm and edge direction.
		- each $v$ maintains shortest path distance to destination $t$, plus the first edge/hop.
	- Handling asynchrony: switch from 'pull-based' to 'push-based' 
		- as soon as $A[i,v] < A[i-1, v]$, $v$ notifies (push) all of its neighbors for updates
		- algorithm guaranteed to converge eventually, **assuming no negative cycles**. Reason: updates decrease shortest distance
	- Handling failures -- when an edge is broken
		- change: each $v$ maintains shortest path distance to destination $t$, plus the ENTIRE PATH. Cons: more space required.

### Floyd-Warshall
compute all pairs of shortest paths (APSP) and report relevant negative cycles if any
-   Time complexity: (n: vertex #;  m: edge #;)
	- $O(n^2m)$ for Bellman Ford
	- $O(nmlogn)$ for Dijkstra
	- $O(n^3)$ for Floyd-Warshall
- Works with negative edges
- better than {n * Bellman Fords} in dense graph ($n<m$)
- with nonnegative edge costs, competitive with {n * Dijkstra's} in  dense graphs
- important special case: transitive closure of a binary relation

### Johnson's Algorithm
compute all pairs of shortest paths (APSP)
-   1 invocation of Bellman Ford + n invocation of Dijkstra: O(mnlogn)
-   Weight each vertex, adjust edge length to E(u, v) = E + Pu -- Pv
-   Weighting vertex, updating edge lengths: (add a new vertex, 1 Bellmon Ford), can still report a negative cycle in original graph
-   N Dijkstra
-   5: For each pair u, v in G, return the shortest path distance d(u, v) = d'(u, v) -- pu + pv
-   Running time: O(1) in step 1, O(mn) in step 2, O(m) in step 3, O(nmlogn) in step 4, O(n\^2) in step 5, total: O(nmlogn).
-   Pro: **handle negative edges, and much better than FloydWarshall, BellmanFord in sparse graphs**

# Summary: Running time for APSP:
- Bellman Ford: $O(n^2m)$
- Dijkstra: $O(nmlogm)$ (negative edges not allowed)
- Floyd Warshall: $O(n^3)$
- Johnson's: $O(mnlogn)$

For sparse graph -> Johnson is best
For dense graph -> Floyd-Warshall is best

