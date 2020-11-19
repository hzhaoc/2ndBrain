from collections import defaultdict


class Graph:
	def __init__(self):
		self._edges = []
		self._G = defaultdict(list)

	def addEdge(self, u, v, cost=0):
		self._G[u].append(v)
		self._G[v].append(u)
		self._edges.append((cost, u, v))  # cost comes first so it can be sorted easily

	@property
	def edges(self):
		return self._edges

	@property
	def vertexes(self):
		return list(self._G.keys())

	@property
	def graph(self):
		return self._G
