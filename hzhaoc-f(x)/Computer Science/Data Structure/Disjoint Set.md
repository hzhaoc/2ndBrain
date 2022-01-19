# Union-find  /  Disjoint Set

### Normal Unions
-   Property
    -   Each vertex/element belongs to a group/cluster/leader
    -   Each vertex/element points to a leader vertex in that group.
    -   this leader is their parent vertex
-   Merge/Union optimize
    -   in each merge, update the smaller sized group's leader
-   Pros & Cons
    -   **Find() takes O(1)** (Find() finds the leader vertex)
    -   **Union() worst case takes O(n)**
    -   In MST, total Union() operations is O(nlogn)

###  Lazy Unions
-   Property similar to Normal Unions except that:
    -   Update only one pointer in each union by making one group's leader a child of the other one
    -   Leader is the root vertex
-   Merge/Union optimize
    -   Union by rank.
	```C++
	S1 = Find(x)
	S2 = Find(y)
	if rank(S1) > rank(S2){
		parent[S2] = S1
	} elif rank(S1) < rank(S2){
		parent[S1] = S2
	} else {
		parent[S2] = S1
		ranks[S1] += 1
	}
	```
-   Update ranks to restore invariant
-   Path compression to optimize find
    -   After Find(x), rewire parent pointers directly to root along the path X-X_Root
    -   Hopcroft-Ullman Theorem
        -   With Union by Rank and Path Compression. In n vertex graph, M union operations take **O(mlog\*n)** time, where log\*n = the number of times you need to apply log to n before the result is \<= 1. E.g. log\* 2\^65536 = 5
        -   I haven't walk through the proof myself yet.
        -   Not optimal yet
    -   Ackerman Function
        -   Tarjar's Bound (theoretical): with union by rank and path compression, In n vertex graph, M union operations take **O(mα(n)),** where α(n) is the inverse Ackerman Function that's even much smaller than **log\*n**

-   Pros & Cons after Optimize
    -   Union() reduces to two Find()
    -   **Find() and Union() worse case takes O(logn)** (Find() finds the leader vertex)

## implementation
- lazy union
```python
class UnionFind:
	"""
	Lazy Union: In union(x, y) function, link x's root's parent to y's root
	total work of m finds (m is # of edges) = O(m* alpha(n))
	"""

	def __init__(self, vertexes):
		"""init union find object from list of numbered vertexes"""
		self._vertexes = vertexes
		self._parents = {x: x for x in self._vertexes}
		self._ranks = {x: 1 for x in self._vertexes}
		self._n_of_union = len(vertexes)

	@classmethod
	def _initfromGraph(cls, graph):
		"""init union find object from class of graph"""
		return cls(graph.vertexes)

	def find(self, x):
		# optimize by Path Compression
		if x == self._parents[x]:
			return x
		return self.find(self._parents[x])

	def union(self, x, y):
		# optimize by Union by Rank
		x_root = self.find(x)
		y_root = self.find(y)
		if x_root == y_root: # already in same group
			return
		self._n_of_union -= 1  # union makes number of unions decrease by 1
		x_rank = self._ranks[x_root]
		y_rank = self._ranks[y_root]
		if x_rank > y_rank:  # make y root point to x root
			self._parents[y_root] = x_root
		elif x_rank < y_rank:  # do opposite
			self._parents[x_root] = y_root
		else:  # x_rank == y_rank, arbitrarily do same as x_rank > y_rank, additionally add 1 to x's root's rank
			self._parents[y_root] = x_root
			self._ranks[x_root] += 1

	def inSameUnion(self, x, y):
		# check if x and y belongs to same union
		return self.find(x) == self.find(y)

	@property
	def parents(self):
		return self._parents
	
	@property
	def ranks(self):
		return self._ranks
	
	@property
	def vertexes(self):
		return self._vertexes

	@property
	def n_of_union(self):
		return self._n_of_union
```

# use
```python
def C3W2_2():
	"""Input nodes of 24 bits. Edge cost is Hamming Distance"""
	"""largest value of k such that there is a k-clustering with spacing at least 3"""
	# input
	i = -1
	with open('data\\clustering_big.txt') as file:
		nodes = []
		for line in file:
			if i == -1:
				i += 1
				continue
			bit = int(''.join(line.split()), 2)  # converted binary to decimal
			nodes.append(bit)
	nodes = set(nodes)  # this equals union nodes with distance = 0 (we only care about distinced nodes in this problem)
	mask1 = [1 << i for i in range(24)]  # 1-bit mask (distance = 1)
	_tmp = [i+1 for i in mask1[1:]]
	mask1 = set(mask1)
	mask2 = {x << i for i in range(24) for x in _tmp if (x << i) <= int('1'*24, 2)}  # 2-bit mask (distance = 2)
	# clustering
	union = UF.UnionFind(nodes)
	for node in nodes:
		# union this node with other nodes where distance = 1
		for m1 in mask1:
			if (node ^ m1) in nodes and not union.inSameUnion(node, node ^ m1):
				union.union(node, node ^ m1)
		# union this node with other nodes where distance = 2
		for m2 in mask2:
			if (node ^ m2) in nodes and not union.inSameUnion(node, node ^ m2):
				union.union(node, node ^ m2)
	# after distance=1 nodes and distance=2 nodes are unioned. Current K is the largest with spacing at least 3
	# if continue union, shortest distance = 3 nodes will be unioned, and K will decrease.
	print(f'current largest K with spacing at least 3 is {union.n_of_union}')
```

```python
def MST_Kruskal(graph):
	"""
	compute MST (minimum spanning tree)
	Kruskal's Algorithm
	high-level description: iteration through edges, find minimal edges in each iteration and add it to MST until MST is completed
	remmeber to check cycles in each iteration to maintain MST property (use union-find to achieve O(1) cycle check)
	Graph Structure: class of graph
	Time Complexity = O(m*log(n))
	"""
	union = UF.UnionFind.__fromGraph(graph.vertexes)
	edges = qsort(graph.edges, 0, len(qsort.edges)-1, pivot='random')
	V = set(graph.vertexes)
	X = set()
	MST = set()
	total_cost = 0
	while X != V:
		edge = edges.pop(0)
		cost = edge[0]
		point1 = edge[1]
		point2 == edge[2]
		if not union.inSameUnion(point1, point2):
			X.add(point1)
			X.add(point2)
			MST.add(edge)
			total_cost += cost
			union.union(point1, point2)
	return MST, total_cost
```

```python
def MaxSpaceClustering(graph, K):
	"""
	max-spacing k-clustering: find max space between two clusters in a K-cluster graph
	implementation is similar to Kruskal's MST algo
	distance/spacing function can be customized. assume edge cost is used
	"""
	union = UF.UnionFind._initfromGraph(graph)
	edges = qsort(graph.edges, 0, len(graph.edges)-1, pivot='random')
	while union.n_of_union > K:
		edge = edges.pop(0)
		cost, point1, point2 = edge[0], edge[1], edge[2]
		if not union.inSameUnion(point1, point2):
			union.union(point1, point2)
	while True:  # find max_space
		edge = edges.pop(0)
		cost, point1, point2 = edge[0], edge[1], edge[2]
		if not union.inSameUnion(point1, point2):
			return edge
```