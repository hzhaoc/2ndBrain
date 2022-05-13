### Minimum Spanning Tree
A minimum spanning tree (MST) or minimum weight spanning tree is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.

### Prim's Algorithm
this is a [[Approaches#Greedy|greedy]] algorithm
```python
def MST_Prim(graph, start):
	"""
	compute MST (minimum spanning tree) Prim's algorithm
	high-level description: starting from one arbitrary vertex, iterate through vertexes, 
	in each iteration, add one vertex to MST which has the minimual local costs, 
	then update spanning vertexes ready for next iteration, similar to shortest paths (Dijkstra's algo)
	it deal with indirected graph, directed graph
	it only tracks total min edge cost for MST. but of course you can also track MST structure.

	@params
	: graph: dicts whose keys are vertexes, values are lists of tuples of (adjacent vertexes, costs)
	: start: arbitrary starting vertex

	time complexity: O(m*logn)
	"""
	V = set(graph.keys()) # all vertexes
	X = set()  # explored vertexes
	pq = [(0, start)]  # priority queue to proceess min cost one at a time in iteration, also spanning vertexes qith edges (vertexes with cross-edges between X and V-X)
	total_cost = 0
	i = 0
	while X != V:
		cur_cost, cur_v = minheap.pop(pq)
		if cur_v in X:  # ignore explored vertexes still in queue
			continue
		X.add(cur_v)
		total_cost += cur_cost
		for neighbor, cost in graph[cur_v]:
			if neighbor in X: # due to heap, if a vertex is already visited, it means its MST edge is already found, so ignore later visists
				continue
			minheap.add(pq, (cost, neighbor))  # add this edge cost and mark this vertex as visited
	return total_cost
```

### Kruskal's Algorithm
this is a [[Approaches#Greedy|greedy]] algorithm
```python
def MST_Kruskal(graph):
	"""
	compute MST (minimum spanning tree)
	Kruskal's Algorithm
	high-level description: iteration through edges, find minimal edges in each iteration and add it to MST until MST is completed
	remmeber to check cycles in each iteration to maintain MST property (use union-find to achieve O(logn) cycle check)
	it tracks both total cost and MST structure
	
	@params
	: graph: dicts whose keys are vertexes, values are lists of tuples of (adjacent vertexes, costs)

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