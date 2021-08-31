# Principal
See also [[Approaches#Dynamic Programming]]
-   Identify a problem's **optimal structure** in relation to its **optimal substructures**, as well as **base cases**
-   Use this relation to breakdown problem and build optimal structure bottom-up

# Examples
### max weight of independent set in graph
-   Denote Gi = first ith vertices of graph G, A\[i\] = value of max Independent Set of Gi
-   Initialize A\[0\] = 0, A\[1\] = w1
-   Loop i = 2, 3, ..., n:

> A\[i\] = max{a\[i-1\], a\[i-2\] + wi}

##### code
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

### knapsack problem
- Input: $n$ items. Each has a positive value $v_i$,  and a size  $w_i$. Also, knapsack capacity $W$.
- Goal: subset $S \in {1,2,...,n}$ that maximizes $\sum_{i\in S}v_i$
- Cons.: $\sum_{i\in S}w_i\leq{W}$ 
##### algorithm 1
- assumes $w_i$ and $W$ are integers. 
- runtime complexity: $O(nW)$ (poly-time if $W$ are polynomial to $n$)
##### code
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

##### Algorithm 2
- assumes $v_i$ are integers 
- run time $O(n^2*max(V_i))$ (poly-time if $max(V_i)$ are polynomial to $n$)
### Sequence alignment
to add

### Optimal Binary Search Tree
See [[Optimal Binary Search Tree]].
- Time Complexity: $O(n^3)$
- Space Complexity: $O(n^2)$

### Shortest-path in graph
- [[Shortest Path#Bellman Ford Algorithm]] $O(n^2m)$
- [[Shortest Path#Floyd-Warshall Algorithm]] $O(n^3)$
- [[Shortest Path#Johnson's Algorithm]] $O(mnlogn)$

For sparse graph $m=O(n)$ -> Johnson is best
For dense graph $m=O(n^2)$ -> Floyd-Warshall is best. Additionally Floyd-Warshall is better for distributed computing.

### Traveling Salesman Tour
find minimum total edge cost of a Cycle that visits each vertex in graph Exactly once. This is an [[NP Complete]] problem.
- time: $O(n^22^n)$
##### code
```python
def TSP(cities, n):
	"""
	minimum Traveling Salesman Tour. 
	An NP-Complete problem.
	time complexity: O(n^2*2^n)
	"""
	s, A, A_pre = 0, {((), 0): 0}, {} # start vertex: 0
	for size in range(1, n): # additional optimal structure subset size
		A_pre, A = copy.deepcopy(A), {}
		for subset in combinations(range(1, n), size): # traverse subset (cycle of vertices) combinations of some size
			theset = tuple(sorted(subset))
			for j in subset: # end vertex: j
				A[(theset, j)] = float("inf")
				for k in (0,) + subset: # like Bellman-Ford, k is the 2nd-last vertex to the last vertex j
					if k != j:
						A[(theset, j)] = min(A_pre.get((tuple(sorted([v for v in subset if v != j])), k), float("inf")) + distance(cities, k, j), A[(theset, j)])
				print(size, subset, j)

	theset, premin = tuple(range(1, n)), float("inf")
	for i in range(1, n):
		_tmp = A[theset, i] + distance(cities, i, 0)
		if _tmp < premin: 
			premin = _tmp
		print(i, _tmp)
	return premin

def distance(cities, k, j):
	x1, y1 = cities[k]
	x2, y2 = cities[j]
	return ((x1-x2)**2 + (y1-y2)**2)**0.5
```