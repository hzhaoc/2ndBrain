from collections import defaultdict
from collections import Counter
from heap import MinHeap
import pandas as pd
import union_find as UF
import graph
from sort import QuickSort as qsort
import tree

minheap = MinHeap()


def MST_Prim(graph, start):
	"""
	compute MST (minimum spanning tree)
	Prim's algorithm
	high-level description: starting from one arbitrary vertex, iterate through vertexes, in each iteration, add one vertex to MST which has the minimual local costs, then update spanning vertexes ready for next iteration
	similar to shortest paths (Dijkstra's algo)
	deal with indirected graph, directed graph
	Graph Structure: dicts whose keys are vertexes, values are lists of tuples of (adjacent vertexes, costs)
	"""
	V = set(graph.keys()) # all vertexes
	X = set()  # explored vertexes
	pq = [(0, start)]  # priority queue to proceess min cost one at a time in iteration, also spanning vertexes qith edges (vertexes with cross-edges between X and V-X)
	total_cost = 0
	i = 0
	while X != V:
		cur_cost, cur_v = minheap.pop(pq)
		if cur_v in X:  # ignore old spanned vertexes still in queue
			continue
		X.add(cur_v)
		total_cost += cur_cost
		for neighbor, cost in graph[cur_v]:  # update spanning vertexes
			if neighbor in X:
				continue
			minheap.add(pq, (cost, neighbor))
	return total_cost


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


def MaxSpaceClustering(graph, K):
	"""
	max-spacing k-clustering
	similar to Kruskal's MST algo
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


if __name__ == '__main__':
	import sys
	import threading
	import time
	threading.stack_size(67108864)  # 64MB stack
	sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
	thread = threading.Thread(target=C3W3_1)  # instantiate thread object
	thread.start()  # run program at target
