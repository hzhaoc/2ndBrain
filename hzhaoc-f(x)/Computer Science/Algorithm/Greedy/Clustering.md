### Minimum Max Space in K-Cluster Graph
find max space between two clusters in a K-cluster graph. this is a [[Approaches#Greedy|greedy]] algorithm

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
