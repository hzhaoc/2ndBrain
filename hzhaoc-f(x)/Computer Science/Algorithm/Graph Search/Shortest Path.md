### Dijkstra’s Algorithm.
compute shortest distance between a starting vertex and all other vertexes in a graph. You can also track shortest path simultaneously, not shown in the code below.

idea is
- starting from target vertex, explore neighbor vertexes by order of cumulative distance (ascending)
- if vertex to be explored is already explored, ignore;
- if vertex to be explored is new, update cumulative distance.

how does this make sure distance to each vertex is minimum?  key is exploration order is by distance. (this is implemented by heap) 

Time Complexity: $O(mlogn)$, m = # of edges, n = # of vertexes

pros:
1. can deal with directed graph, undirected graph, non-negatives paths

cons:
1. can't be applied to negative edge lengths (can be improved. See below code implementation)
2. not very distributed (relevant to Internet routing)

##### Code Implementation
```python
class Graph:
	def __init__(self, adjacencyList=None):
		if not adjacencyList:
			self.G = defaultdict(list)
			self.G_rev = defaultdict(list)
		else:
			self.G = adjacencyList

	def addEdge(self, u, v):
		self.G[u].append(v)
		self.G_rev[v].append(u)
		return

	# add edge with length
	def addEdgeLen(self, u, v, l):
		self.G[u].append((v, l)) 
		return

	def minDist(self, start):
		'''
		Dijkstra’s Algorithm. compute shortest distance between a starting vertex and all other vertexes in a graph
		
		input graph data structure: dict. key is vertex, value is a list of tuples (adjacent vertex i, distance i)
		v, l = graph[u][j]: vertex u's jth adjacent vertex is vertex v at distance l

		'''
		maxdist = float('inf')
		dists = {v: maxdist for v in self.G.keys()}  # initialize all vertex distance to start vertex to be infinite, (start vertex itself is 0)
		seen = set()
		# lth = len(self.G.keys())
		pq = [(0, start)]  # initiate cuts with priority queue (heap) from a starting vertex, and distance 0
		while pq:  # all V to V-X vertexs (include inner V because this algo doesn't delete old edges) 
			cur_dist, cur_v = heapq.heappop(pq)  # ensure min distance poped out for one vertex at a time in vertex interation
			if cur_v in seen:  # ignore explored vertex
				continue
			dists[cur_v] = cur_dist  # update min distance for this vertex
			seen.add(cur_v)  # mark current vertex as explored
			for neighbor, weight in self.G[cur_v]:  # insert new edges into queue (to compute min distance in next iteration)
				if neighbor in seen:
					continue
				dist = cur_dist + weight
				heapq.heappush(pq, (dist, neighbor))
		return dists
		
	def NewminDist(self, start):
		'''
		compute shortest distance between a starting vertex and all other vertexes in a graph
		deal with negative paths? 
		Improved Dijkstra’s Algorithm
		Time Complexity: depends on negative paths? might run into infinite loops?
		'''
		maxdist = float('inf')
		dists = {v: maxdist for v in self.G.keys()}
		dists[start] = 0
		pq = [(0, start)]
		while pq:
			cur_dist, cur_v = heapq.heappop(pq)
			if cur_dist > dists[cur_v]:
				continue
			for neighbor, weight in self.G[cur_v]:
				dist = cur_dist + weight
				if dist < dists[neighbor]:
					dists[neighbor] = dist  # if negative weight, min distance might be updated here
					heapq.heappush(pq, (dist, neighbor))
		return dists
```