from collections import defaultdict
from collections import Counter
import heapq


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
		Dijkstra’s Algorithm.
		compute shortest distance between a starting vertex and all other vertexes in a graph
		deal with directed graph, undirected graph, non-negatives paths
		Time Complexity: O(nlogm), m = # of edges, n = # of vertexes
		
		this algorithm doesn't deal with negative distance
		input graph is made of adjacency lists
		data structure: tuple of list of dict
		v, l = graph[u][j]: jth adjacent vertext to vertex u is vertex v at length l
		cons:
		1. can't be applied to negative edge lentghts
		2. not very distributed (relevant for Internet routing)
		'''
		maxdist = float('inf')
		lth = max(self.G.keys())
		dists = {v: maxdist for v in self.G.keys()}  # initialize all vertex distance to start vertex to infinite, (start vertex itself is 0)
		seen = set()
		lth = len(self.G.keys())
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
		lth = max(self.G.keys())
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

	# compute storngly-connected-components, Kosaraju’s algorithm
	def ComputeSCC(self):
		lth = max(self.G.keys())
		print('graph nodes number', lth)
		# DFS-LOOP 1
		self.visited = [False] * (lth + 1)
		self.finish = []
		self.t = 0
		for v in reversed(range(1, lth + 1)):
			if not self.visited[v]:
				self._DFSf_recur_2(v)
		# DFS-LOOP 2
		self.visited = [False] * (lth + 1)
		self.leaders = []
		for v in reversed(self.finish):
			if not self.visited[v]:
				leader = v
				self._DFS_recur_2(v, leader)

	def SortedSCCSize(self, top):
		leaders = self.leaders
		count = Counter(leaders)
		res = count.most_common()[:top]
		return res

	def _DFS_iter(self, graph, start, path):
		stack = list()
		stack.append(start)
		while stack:
			vertex = stack.pop()
			path.append(vertex)
			nextVertexs = graph[vertex]
			for v in nextVertexs:
				if v not in path:
					stack.append(v)
		return path

	def _DFSf_iter(self, graph, start, path, finish):  # with finish times
		stack = list()
		stack.append(start)
		while stack:
			vertex = stack.pop()
			if vertex not in path:
				path.append(vertex)
				stack.append(vertex)
				nextVertexs = graph[vertex]
				for v in nextVertexs:
					if v not in path:
						stack.append(v)
			else:
				if vertex not in finish:
					finish.append(vertex)
		return path, finish

	def _DFS_recur(self, graph, vertex, path):
		path.append(vertex)
		for nextVertex in graph[vertex]:
			if nextVertex not in path:
				path = self._DFS_recur(graph, nextVertex, path)
		return path

	def _DFSf_recur(self, graph, vertex, path, finish):  # first DFS_recur method wit finish times
		path.append(vertex)
		for nextVertex in graph[vertex]:
			if nextVertex not in path:
				path, finish = self._DFSf_recur(graph, nextVertex, path, finish)
		if all([x in path for x in graph[vertex]]):
			finish.append(vertex)
		return path, finish

	def _DFS_recur_2(self, s, leader):
		self.visited[s] = True
		for v in self.G[s]:
			if not self.visited[v]:
				self._DFS_recur_2(v, leader)
		self.leaders.append(leader)
		return

	def _DFSf_recur_2(self, s):  # second DFS_recur method with finish times 
		self.visited[s] = True
		for v in self.G_rev[s]:
			if not self.visited[v]:
				self._DFSf_recur_2(v)
		self.finish.append(s)
		return


##############################################################
def C2W1():
	graph = Graph()
	with open('SCC.txt') as file:
		for line in file:
			edge = line.split()
			graph.addEdge(int(edge[0]), int(edge[1]))
	graph.ComputeSCC()
	print(graph.SortedSCCSize(5))


def C2W2():
	graph = Graph()
	g = {}
	with open('data\\dijkstraData.txt') as file:
		for line in file:
			temp = line.split()
			g[int(temp[0])] = [tuple(int(j) for j in i.split(',')) for i in temp[1:]]
	graph.G = g
	dists = graph.minDist(1)
	V = '7,37,59,82,99,115,133,165,188,197'
	V = [int(v) for v in V.split(',')]
	res = []
	for v in V:
		res.append(str(dists[v]))
	res = ','.join(res)
	print(res)


def C3W1():
	graph = Graph()
	g = {}
	g[1] = [(2, 3), (3, 2)]
	g[2] = [(3, -2)]
	g[3] = []
	graph.G = g
	dists = graph.NewminDist(1)
	res = dists
	print(res)


if __name__ == '__main__':
	import sys
	import threading
	import time
	threading.stack_size(67108864)  # 64MB stack
	sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
	thread = threading.Thread(target=C3W1)  # instantiate thread object
	thread.start()  # run program at target
