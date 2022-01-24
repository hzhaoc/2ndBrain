### Strongly Connected Component
A directed graph is called strongly connected if there is a path in each direction between each pair of vertices of the graph. It is possible to test the strong connectivity of a graph, or to find its **Strongly Connected Components** (SCCs), in linear time (that is, Θ(V + E)).

### Topological Sort
In computer science, a topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.  

Mathematically, in graph A,  for each edge u->v, order(u) < order(v) 

Statement "**a directed graph has a topological ordering**" is sufficient and necessary for statement "**a directed graph is acyclic**"

### Kosaraju’s algorithm
First notice a few things:
- A DAG (directed acyclic graph) always has at least one **sink vertex** (that is a vertex with not directed edges going out).
- SCC level graph of a DAG graph, or "meta-graph", is a **DAG**, and therefore has at least one **sink SCC**. Shown below:
![[SCC1.jpg|600]] ![[SCC2.jpg|600]]
- A graph and its direction-reversed graph (**reverse graph**) have **same SCCs**, just pointing to opposite directions.
- A good DFS at a vertex could return a SCC, if this selected vertex is **inside** the Sink SCC.
- A bad DFS at a vertex could not return a SCC, if this selected vertex is outside the Sink SCC.

Therefore, to get SCCs, the question becomes: **how to always start DFS at Sink SCC to find one SCC after another?**

The answer in Kosaraju's Algorithm is: we need a **topological order of the graph at SCC level**, then we do a vertex traversal with DFS in the reverse of this topological order (latest SCC first, earliest SCC last). This way, it is guaranteed that each vertex traversed (which is the start vertex for one DFS) will be inside **Sink SCC**, and for each DFS, we get a SCC. This **SCC level topological order** can be first obtained by another random order vertex traversal with DFS on reverse graph (or original graph I think since SCC topological order is just opposite to each other) where the **SCC topological order is tracked **

##### Code Implementation
```python
class Graph:
	def __init__(self, vertices): # input is list of vertex indexes
		self.V = vertices
		self.G = {v: set() for v in vertices}
		self.G_rev = {v: set() for v in vertices}

	def addEdge(self, u, v):
		self.G[u].add(v)
		self.G_rev[v].add(u)

	def ComputeSCC(self):
		"""
		compute storngly-connected-components, Kosaraju’s algorithm
		@input self.G, self.G_rev: graph in dictionary where key is vertex, value is list of its adjacent vertices
		@return 
		: self.finish: list of vertices in SCC-level topological order / finish time order
		: self.leaders: list of leaders, a vertice in self.finish can find its leader/SCC group in same position in self.leaders 
		"""
		# DFS-LOOP 1
		self.visited, self.finish = set(), []
		for v in self.V[::-1]: # this order does not matter, its random
			if v != 0 and v not in self.visited:
				self._DFSf_recur_2(v)
		# DFS-LOOP 2
		self.visited, self.leaders = set(), dict()
		for leader in self.finish[::-1]:
			if leader not in self.visited:
				self._DFS_recur_2(leader, leader)

	def _DFS_recur_2(self, s, leader):
		self.visited.add(s)
		for v in self.G[s]:
			if v not in self.visited:
				self._DFS_recur_2(v, leader)
		self.leaders[s] = leader

	def _DFSf_recur_2(self, s): # second DFS_recur method with finish times 
		self.visited.add(s)
		for v in self.G_rev[s]: # not necessarily reverse graph, original graph is ok, just opposite order of finish times / SCC topological order
			if v not in self.visited:
				self._DFSf_recur_2(v)
		self.finish.append(s)
```

### Uses
#####  Structure of the web
Many interesting researches at going on with the structure of the web. It is presented that modern web structure is shaped like a bow-tie shown below. (2012). 
-  25% of webs are located in the giant core SCC
-  25% of webs are in "in" part of separate SCCs.
-  25% of webs are in "out" part of separate SCCs.
-  25% of webs are remains: tendrils, and outliers?

![[web structure - bow tie.png|500]]

