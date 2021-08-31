find shortest path and distance in a directed/undirected graph {vertex, edge}
# Dijkstra’s Algorithm
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
1. can't be applied to negative edge lengths (can be improved?. See below code implementation)
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

# Bellman Ford Algorithm
Either compute a shortest cycle-free path $s-v$ or output a negative cycle, for all paths starting from $s$. This is a [[Dynamic Programming]] solution.

##### identify optimal sub-structures & base cases
Since subpath of a shortest path is in itself a shortest path, for a shortest path s-v, it can be broken down into shortest of all shortest paths w-v (w is any adjacent vertex of v's) plus its last edge cost C(w,v). Is this enough? When the structure is broken down into sub-structures, we notice number of edges in the subpath decrease by 1. And this information needs to be reflected in the program. Therefore, we assign a budget (number of edges needed at maximum) for any structure of shortest path s-v. Easily known, this budget is no bigger than vertex # -  1. And we have our base cases $A[x, s] = 0$, which means shortest distance s-s with any number of edges is 0. Remaining elements in $A$ will be initialized to $+\infty$. Also notice with budget introduced, there's also a case when $A[v,  i] = A[v,i-1]$ when $i$ number of edges is enough for optimal path $s-v$ 

##### pseudo code & analysis
- Let $L_{i,v}$ = minimum length of a $s-v$ path with edge number $n\leq{i}$. $l_{i, j}$ = edge length of $e(i, j)$. Cycles allowed. And $+ \infty$ if no such path exists
	- For $i = 1, 2, ..., n-1$: ($n$ if one (**only one!**) negative cycle existence needs to be checked) 
		- For $v = 1, 2, ..., n$:
			- $$L_{i,v}=\min\left\{ \begin{matrix} L_{\left( i - 1 \right),\ v} \\ \min_{(w,v) \in E}\left\{ L_{\left( i - 1 \right),w} + l_{w,v} \right\} \\  \end{matrix} \right.\ $$
			- meanwhile, keep track of Predecessor pointers $B[i, v]$ = 2nd-last vertex in the shortest path. this will track shortest paths. note that $B[0, v] = null$.
			- with no negative cycles:  if $L_{i, v}=L_{i-1, v}$ ($v$ is target vertex). This means optimal path is already found for path $s-v$. Can exit early. 
			- *if only need to check negative cycle: check last iteration (n) and see if there's improvement in distance; if also need to find the negative cycle path: use DFS to check for a cycle of predecessor pointers at every iteration*.

> Why only one more iteration is sufficient to **one** capture negative cycles in shortest path? 
> - If there's **1** negative-cycle in shortest s-v, one of the vertex in the path Must be visited Twice, number of edges for the budget will increase by one. n-1 => n.
> - Extension: I think **K** additional iterations on top of original 0 -> n-1 will be able to capture K negative cycles in the shortest path s-v, since one negative cycle makes one vertex visited one more time, increasing edge number budget by 1.

- Time Complexity is $O(mn)$ without negative edges.

> Why it is not the intuitive answer $O(n^2)$?
> total work is $O(n*\sum_{v\in{V}}{\text{in-degree}(v)})$ = $O(n*m)$

- Space Complexity: $O(n^2)$
	- Space optimization: 
		- only need $A[i-1, v]$ to compute $A[i, v]$ for any $v$ in vertexes. $O(n)$
		- if only check negative cycle, $B$ also needs only $O(n)$. if need to store the path, still need $O(n^2)$ for $B[i, v]$.
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

##### code
```python
def BellmanFord(G, n):
	"""
	Bellman Ford algorithm to compute shortest paths of all pairs, given Graph and number of vertexes
	time complexity: O(n^2m), m is # of edge, n is # of vertex. (slow. 23200s on (V, E)~(1k, 50k))
	space compelxity: O(n)

	assignment is to check either existence of negative cycle or smallest shortest distances of all pairs
	note: input graph is 1-indexed, but the algorithm is 0-indexed
	"""
	global_d_min = float("inf")

	for s in range(n): # tail vertex
		# start of one BellmanFord.
		L = [[float("inf") if i!=s else 0 for i in range(n)] for j in range(2)] # L[head][max edge #] = shortest distance
		# B = [[None for i in range(n)] for j in range(2)] # B[u][i] = shortest-path (s,v)'s 2nd-last vertex with edge # <= i for path construction 
		for i in range(1, n+1): # budeget of edge #. 0 for base case; n for negative cycle case.
			curi, prei = i%2, 1-i%2 # flip index 
			for v in range(n): # head vertex
				L[curi][v] = L[prei][v]
				# B[curi][v] = B[prei][v]
				for w in G.G_rev[v+1]:
					if L[prei][w-1] + G.C[(w, v+1)] < L[curi][v]:
						L[curi][v] = L[prei][w-1] + G.C[(w, v+1)]
						# B[curi][v] = w-1
				if i==n:
					if L[curi][v] < L[prei][v]: return 0, None # check negative cycle
					if s != v and L[curi][v] < global_d_min: global_d_min = L[curi][v] # assignment: track global min of all shortest distances
		# end of one BellmanFord.
		print("progress: {0:.2f}%".format((s + 1) * 100 / n), end="\r")
	return 1, global_d_min
```


# Floyd-Warshall Algorithm
compute all pairs of shortest paths (APSP) and report relevant negative cycles if any. This is a [[Dynamic Programming]] solution.

##### identify optimal sub-structures
we know a subpath of a shortest path is in itself a shortest path. This time we don't break down an optimal path into a sub-optimal path and last edge, but two shortest paths (with a shared intermediary internal vertex of course). Notice also during this breakdown, for internal vertices of a path, the shared vertex is out. If we pre-index the vertexes 1, 2, ..., n, then during the optimal sub-structure breakdown, we can search for $f(K)$ which denotes vertexes 1 to K used for an optimal structure. If vertex $K$ is an internal vertex for the optimal path A[s, v, K] (denoting optimal distance between s and v,  with 1,2,...,K vertex as internal vertices), then its two optimal sub-paths will be exactly $A[s,k-1,k-1]$ and  $A[k+1,v,k-1]$. 

Base cases & initialization: 
- $A[s,s,0]=0$
- if $(s-v)\in{E}$: $A[s,v,0]=C(s,v)$
- for remaining $(s,v)$: $A[s,v,0]=\infty$

Also notice with budget introduced, there's also a case when $A[s,v,k]=A[s,v,k-1]$ when $1,2,...k-1$ internal vertexes are enough for optimal path $s-v$ 

##### pseudo code & analysis
```C
preindex vertices as 1,2,...,n
let A[s,v,K] denote shortest distance s-v, with internal vertices 1,2,...K. 
let B[s,v] denote max index in its internal vertices.

for k=1 to n:
	for i=1 to n:
		for j=1 to n:
			A[i,j,k] = min{A[i,j,k-1], A[i,k,k-1] + A[k,j,k-1]}
			B[i,j] = k if A[i,j,k] gets updated // it means k is an internal vertex to path i-j
```

- what about negative cycles?
	- when the algorithm is run, check $A[i,i,k]$ for any $i, k$.  If one of them is **negative**, negative cycle exists.
-   Time complexity: 
	-   $O(n^3)$ (n: vertex #;  m: edge #;)
- important special case: transitive closure of a binary relation (basically means you only need to check if two vertexes s-v has a path.). specifically,  change one line to 
```C
			A[i,j,k] = min{A[i,j,k-1], A[i,k,k-1] * A[k,j,k-1]}
```

##### code
```python
def FloydWarshall(G, n):
	"""
	Floyd Warshall algorithm to compute shortest paths of all pairs, given Graph and number of vertexes
	time complexity: O(n^3), m is # of edge, n is # of vertex (okay. 600s on (V, E)~(1k, 50k))
	space compelxity: O(n^2)

	assignment is to check either existence of negative cycle or smallest shortest distances of all pairs
	note: input graph is 1-indexed, but the algorithm is 0-indexed
	"""
	global_d_min = float("inf")
	A = [[[G.C[(u+1,v+1)] if ((u+1,v+1) in G.C and k==0) else 0 if (u==v and k==0) else float("inf") for v in range(n)] for u in range(n)] for k in range(2)] # A[internal max][tail][head] = shortest distance
	# B[u][v] = max internal vertex for path construction 

	for k in range(n): # internal max vertex
		curi, prei = 1-k%2, k%2 # flip predecessor
		for u in range(n): # tail
			for v in range(n): # head
					A[curi][u][v] = min(A[prei][u][v], A[prei][u][k] + A[prei][k][v])
					if k == n-1 and u != v and A[curi][u][v] < global_d_min: global_d_min = A[curi][u][v] # assgiment: track global min of shortest distances of all pairs
					if u==v and A[curi][u][v] < 0: return 0, None # check negative cycle
		print("progress: {0:.2f}%".format(k * 100 / n), end="\r")
	return 1, global_d_min
```


# Johnson's Algorithm
compute all pairs of shortest paths (APSP). This is a [[Dynamic Programming]] solution.
##### motivation
running time wise, n\*Dijkstra is better than n\*Bellman Ford, but Dijkstra can not deal with negative edges. And only in dense graph ($n=O(m^2)$), Floyd-Warshall is better than n\*Dijkstra. So how to apply fast Dijkstra with negative edges in graph?
-   Time complexity: (n: vertex #;  m: edge #;)
	- $O(n^2m)$ for n\*Bellman Ford
	- $O(nmlogn)$ for n\*Dijkstra
	- $O(n^3)$ for Floyd-Warshall
##### core idea
reweight edge costs **in a way** that makes:
- there's no negative edges, so we can use Dijkstra which is fast in sparse graph
- new shortest path is the same path as before, so reweighting does no change the answers

but how?
-  consider assign an weight to each vertex, denoted as $w_v$, and modify edge costs to $c'(u,v)=c(u,v)+w_u-w_v$. to calculate a new shortest path distance: $D'(u,v)=D(u,v)+w_u-w_v$ for any $(u,v)$ pair in the modified graph. (all internal terms are canceled through tail-to-head). this means shortest path for $(u,v)$ does not change. Also all edges related to $s$ are outbound so it won't affect shortest-path algorithm.

yet how to assign such weights?
-  notice that if we arbitrarily add an additional vertex $s$, with only outgoing edges to each of original vertices with $0$ distance, run a Bellman Ford on $s$, assign weight $w_v$ to each original vertex $v$ so that $w=D(u,v)$ for any $s,v$pair, where $D(s,v)$ is shortest path distance between $s,v$. Then in the modified graph, new shortest distance $D'(u,v)=D(u,v)+w_u-w_v > 0$. 

why new edges are guaranteed to be non-negative?
- consider any edge $e(u,v)$. After adding new vertex $s$ and reweighting:
	- if $u$ is the 2nd-last vertex in the shortest path $(s,v)$: $$C'(u,v)=C(u,v)+D(s,u)-D(s,v)=C(u,v)+D(s,u)-(D(s,u)+C(u,v))=0$$
	- if $u$ is NOT the 2nd-last vertex in the shortest path $(s,v)$, say it is $t$.  
		- we know $$D(s,u)+C(u,v)\geq D(s,t)+C(t,v)$$
		- for new edge cost, we have $$C'(u,v)=C(u,v)+D(s,u)-D(s,v)$$
		- then $$C'(u,v)\geq [D(s,t)+C(t,v)-D(s,u)]+D(s,u)-D(s,v)=D(s,t)+C(t,v)-D(s,v)=D(s,v)-D(s,v)=0$$
		- thus we proved, for any edge in graph $G$, new edge cost will be non-negative.


##### pseudo code & analysis
1. add new vertex $s$, outgoing arc to each original vertex with distance **0**. 
2. run 1 Bellman Ford on $s$. 
3. assign weights to each vertex $v$ = shortest distance $D(s,v)$. edit new edge cost = old edge cost + tail weight - head weight
4. run N Dijkstra for the graph on new edge costs. then you get all pairs of shortest paths. reverse edit shortest path distance by actual distance = new distance + head weight - tail weight

- dominate run time is at step 4. $O(nmlogn)$
- compare it to other algorithms, it is fast at $O(nmlogn)$, and deal with negative edges.

##### code
```python
def Johnson(G, n):
	"""
	Johnson's algorithm to compute shortest paths of all pairs, given Graph and number of vertexes
	time complexity: O(mnlogn). m is # of edge, n is # of vertex. (fastest. 173s on (V, E)~(1k, 50k))
	space complexity: O(m)

	assignment is to check either existence of negative cycle or smallest shortest distances of all pairs
	note: input graph is 1-indexed same as the array in the algorithm with the new vertex indexed at 0
	"""
	heapq = MinHeap()
	global_d_min = float("inf")

	# do 1 BellmanFord on newly added vertex "0" and reweight all edge costs
	for v in range(1, n+1):
		G.addEdge(0, v, 0)

	L = [[float("inf") if i!=0 else 0 for i in range(n+1)] for j in range(2)] # vertex weights. L[head][edge #]
	for i in range(1, n+1): # edge #. 0 for base case; n for negative cycle case.
		curi, prei = i%2, 1-i%2
		for v in range(n+1): # head
			L[curi][v] = L[prei][v]
			for w in G.G_rev[v]:
				if L[prei][w] + G.C[(w, v)] < L[curi][v]: L[curi][v] = L[prei][w] + G.C[(w, v)]
			if i==n and L[curi][v] < L[prei][v]: return 0, None # check negative cycle
	
	for (u, v) in G.C:
		G.C[(u, v)] += L[curi][u] - L[curi][v] # new cost = old cost + tail weight - head weight

	# do n Dikistra on original vertices
	for s in range(1, n+1): # tail
		# start of 1 Dikistra
	    dists = {v: float('inf') if v != s else 0 for v in range(1, n+1)}
	    seen = set()
	    pq = [(0, s)]
	    while pq:
	        cur_dist, cur_v = heapq.pop(pq) # heap pops min edge
	        if cur_v in seen: continue # ignore explored vertex
	        dists[cur_v] = cur_dist  # update min distance for this vertex
	        if s != cur_v and cur_dist + L[curi][cur_v] - L[curi][s] < global_d_min: # assignment: track global min of shortest distances of all pairs
	        	global_d_min = cur_dist + L[curi][cur_v] - L[curi][s]
	        seen.add(cur_v)  # mark this vertex as explored
	        for neighbor in G.G[cur_v]:
	            if neighbor in seen: continue
	            dist = cur_dist + G.C[(cur_v, neighbor)]
	            heapq.add(pq, (dist, neighbor)) # push new (possible distance, head) to heap
	    # end of 1 Dikistra
	    print("progress: {0:.2f}%".format((s+1) * 100 / n), end="\r")
	return 1, global_d_min
```


# Summary
- Bellman Ford: $O(n^2m)$
- Dijkstra: $O(nmlogn)$ (**X** deal with negative edges)
- Floyd Warshall: $O(n^3)$
- Johnson's: $O(mnlogn)$

For sparse graph $m=O(n)$ -> Johnson is best
For dense graph $m=O(n^2)$ -> Floyd-Warshall is best