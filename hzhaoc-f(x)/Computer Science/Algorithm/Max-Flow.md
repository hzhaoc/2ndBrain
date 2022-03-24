Given a flow network, i.e. a directed graph G=(V, E), and source node s, target node t, and capacity for each edge, compute max of total flow from s to t.
- for each edge, its flow is no greater than its capacity
- for each vertex, its total input flow is equal to its total output flow

### Ford-Fulkerson
1. initialize residual network Gf  for current flow of 0
	1. a residual graph Gf is flow network, where for an original edge (u, v) in graph:  0< f(u, v) < capacity(u, v) and 0< f(v, u) < capacity(u, v) - f(u, v) 
2. check for all s-t paths in Gf, for each such path, 
	- find min capacity in the path in Gf
	- if min capacity > 0:
		- augment flow by this min capacity and update Gf
3. if there's no flow augmentation, exits. Else, repeat step 2. 

##### run time
assume flows are constrained to be integers, run time is O(mC) where C is max flow of s-t, m is number of edges. 
##### code example
```python
class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)
 
    def BFS(self, s, t, parent):
        visited = [False]*(self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:  # ensures capacity > 0
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
        return False
             
    def FordFulkerson(self, source, sink):
        parent = [-1]*(self.ROW)
        max_flow = 0

        while self.BFS(source, sink, parent):
			# augument flow = min capacity in path s-t in residual network
            path_flow = float("Inf")
            v = sink
            while(v != source):
                path_flow = min(path_flow, self.graph[parent[v]][v])
                v = parent[v]
            max_flow += path_flow

			# update residual network
            v = sink
            while(v != source):
                self.graph[parent[v]][v] -= path_flow
                self.graph[v][parent[v]] += path_flow
                v = parent[v]
 
        return max_flow
```

# Min-Cut problem
- input: flow network
- output: st-cut (L, R) with min capacity

##### Theorem
size of max-flow = min capacity of a st-cut

# Generalized Max-Flow problem
Given graph G(V, E), s, t, with capacity and also demand (min capacity required) for each edge, check if there's a flow that meet requirement. We can reduce this to Max-Flow problem by modifying original graph as below:
- for each original edge, new capacity = old capacity - demand
- new source vertex s', connecting to each original vertex, each edge capacity = total demand that goes into that connected vertex
- new target vertex t', connecting to each original vertex, each edge capacity = total demand that goes out from that connected vertex
- an additional edge from t' to s' with capacity to infinity

# Edmonds-Karp algorithm
similar to Ford-Fulkerson's, difference is in step 2, do BFS only, and insert/remove edge. each edge is inserted/removed at most n//2 times, total run time is then guaranteed to be O(m^2n)
1. initialize residual network Gf  for current flow of 0
	1. a residual graph Gf is flow network, where for an original edge (u, v) in graph:  0< f(u, v) < capacity(u, v) and 0< f(v, u) < capacity(u, v) - f(u, v) 
2. **BFS** check for all s-t paths in Gf, for each such path, 
	- find min capacity in the path in Gf
	- if min capacity > 0:
		- augment flow by this min capacity and update Gf
		- **add/remove edge
			- if available capacity decreased to 0, remove this edge
			- if available capacity decreased from max to some value, add reverse edge back**
1. if there's no flow augmentation, exits. Else, repeat step 2. 

```python
#Edmonds-Karp Algorithm
def max_flow(C, s, t):
	n = len(C) # C is the capacity matrix
	F = [[0] * n for i in xrange(n)]
	path = bfs(C, F, s, t)
	# print path
	while path != None:
		flow = min(C[u][v] - F[u][v] for u,v in path)
		for u,v in path:
			F[u][v] += flow
			F[v][u] -= flow
		path = bfs(C, F, s, t)
	return sum(F[s][i] for i in xrange(n))

#find path by using BFS
def bfs(C, F, s, t):
	queue = [s]
	paths = {s:[]}
	if s == t:
		return paths[s]
	while queue:
		u = queue.pop(0)
		for v in xrange(len(C)):
			if(C[u][v]-F[u][v]>0) and v not in paths:
				paths[v] = paths[u]+[(u,v)]
				print paths
				if v == t:
					return paths[v]
				queue.append(v)
	return None
```