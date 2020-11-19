from collections import defaultdict
import copy


def MaxWeightIS(weights):
	"""max weight of independant sets from vertices (0-indexed array of vertice weights)"""
	A = dict()
	A[0], A[1] = 0, weights[0]
	for i in range(2, len(weights) + 1):
		A[i] = max([A[i-1], A[i-2] + weights[i-1]])  # A[i] = the value of max-weight of first ith vertices
	i = len(weights)
	w = dict(zip(range(1, len(weights)+1), [0]*len(weights)))  # w[i] = 1 or 0 indicates if ith vertice is in MWIS
	while i >= 2:
		if A[i-1] >= A[i-2] + weights[i-1]:  # wi not in MWIS
			i -= 1
		else:  # wi in MWIS
			w[i] = 1
			i -= 2
	w[1] = 1 if not w[2] else 0
	return w, A


def Knapsack(vertices, capacity):
	"""Knapsack problem, vertices: array of (weight, size), 0-indexed"""
	A = [[0 for x in range(capacity+1)] for i in range(len(vertices)+1)]  # A[i][j] represents max weights/values for first ith vertices with capacity = j
	for i in range(1, len(vertices)+1):
		for s in range(capacity+1):
			A[i][s] = _knapsack(A, i, s, vertices)
	return A[len(vertices)][capacity]


def _knapsack(A, i, x, vertices):
	wi, si = vertices[i-1]  # weight, size of ith vertice (1-indexed)
	return max([A[i-1][x], A[i-1][x-si] + wi]) if x-si >= 0 else A[i-1][x]


def Knapsack_r(vertices, capacity, i):
	"""Knapsack problem, recursive version"""
	if i < 0:
		return 0
	w, s = vertices[i]
	if capacity < s:
		return Knapsack_r(vertices, capacity, i-1)
	else:
		return max(Knapsack_r(vertices, capacity - s, i-1) + w, Knapsack_r(vertices, capacity, i-1))


def Knapsack_fast(vertices, capacity):
	"""Knapsack problem, vertices: array of (weight, size), 0-indexed, minimum space storage"""
	A, pre_A = [0 for x in range(capacity+1)], [0 for x in range(capacity+1)]
	for i in range(1, len(vertices)+1):
		wi, si = vertices[i-1]
		print(i)
		for s in range(capacity+1):
			A[s] = pre_A[s] if s-si < 0 else max([pre_A[s], pre_A[s-si] + wi])
		pre_A = [x for x in A]
	return A[capacity]


def BellmanFord(graph, s):
	"""
	Bellman Ford algorithm to compute shortest paths, given a graph and a start vertex
	time complexity: O(mn), m is # of edge, n is # of vertex
	"""
	return


if __name__ == "__main__":
	l = [1,2,3]
	print(l[1])