from collections import defaultdict
from collections import Counter
from heap import MinHeap
import pandas as pd
import union_find as UF
import graph
from sort import QuickSort as qsort
import tree
from greedy import MST_Prim, MST_Kruskal, MaxSpaceClustering
from DP import MaxWeightIS, Knapsack, Knapsack_r, Knapsack2


# schedule jobs
def C3W1_1():
	df = pd.DataFrame(columns=['w', 'l'])
	i = -1
	with open('data\\jobs.txt') as file:
		for line in file:
			if i == -1:
				i += 1
				continue
			[w, l] = line.split()
			df.loc[i, 'w'] = int(w)
			df.loc[i, 'l'] = int(l)
			i += 1
	df['diff'] = df['w'] - df['l']
	df['ratio'] = df['w']/df['l']
	df.sort_values(by=['ratio', 'w'], ascending=False, inplace=True)
	df['l_cumsum'] = df['l'].cumsum()
	df['C'] = df['w'] * df['l_cumsum']	
	print(df)
	res = sum(df['C'])
	print('sum of weighted completion times is ', res)
	return res


# Prim MST problem
def C3W1_3():
	i = -1
	with open('data\\edges_MST.txt') as file:
		graph = defaultdict(list)
		for line in file:
			if i == -1:
				i += 1
				continue
			[node_1, node_2, cost] = line.split()
			graph[int(node_1)].append((int(node_2), int(cost)))
			graph[int(node_2)].append((int(node_1), int(cost)))
			i += 1
	res = MST_Prim(graph, 1)
	# res = graph[1]
	print(res)
	

# Max-spacing K-clustering (similar to Kruskal's MST) problem
def C3W2_1():
	i = -1
	with open('data\\clustering1.txt') as file:
		G = graph.Graph()
		for line in file:
			if i == -1:
				i += 1
				continue
			[vertex1, vertex2, cost] = line.split()
			G.addEdge(u=int(vertex1), v=int(vertex2), cost=int(cost))
	max_space = MaxSpaceClustering(graph=G, K=4)
	print(max_space)


def C3W2_2():
	"""Input nodes of 24 bits. Edge cost is Hamming Distance"""
	"""largest value of k such that there is a k-clustering with spacing at least 3"""
	# input
	i = -1
	with open('data\\clustering_big.txt') as file:
		nodes = []
		for line in file:
			if i == -1:
				i += 1
				continue
			bit = int(''.join(line.split()), 2)  # converted to decimal
			nodes.append(bit)
	nodes = set(nodes)  # this equals union nodes with distance = 0 (we only care about distince nodes in this problem)
	mask1 = [1 << i for i in range(24)]  # 1-bit mask (distance = 1)
	_tmp = [i+1 for i in mask1[1:]]
	mask1 = set(mask1)
	mask2 = {x << i for i in range(24) for x in _tmp if (x << i) <= int('1'*24, 2)}  # 2-bit mask (distance = 2)
	# clustering
	union = UF.UnionFind(nodes)
	for node in nodes:
		# union this node with other nodes where distance = 1
		for m1 in mask1:
			if (node ^ m1) in nodes and not union.inSameUnion(node, node ^ m1):
				union.union(node, node ^ m1)
		# union this node with other nodes where distance = 2
		for m2 in mask2:
			if (node ^ m2) in nodes and not union.inSameUnion(node, node ^ m2):
				union.union(node, node ^ m2)
	# after distance=1 nodes and distance=2 nodes are unioned. Current K is the largest with spacing at least 3
	# if continue union, shortest distance = 3 nodes will be unioned, and K will decrease.
	print(f'current largest K with spacing at least 3 is {union.n_of_union}')


# create Huffman codes
def C3W3_1():
	symbols = []
	i, j = -1, -1
	with open('data/huffman.txt') as file:
		for line in file:
			i += 1
			j += 1
			if i == 0:
				continue
			symbols.append((int(line), j))
	hTree = tree.HuffmanTree()
	hTree.encode(symbols)
	print('max depth', hTree.maxDepth)
	print('min depth', hTree.minDepth)
	print('avg depth', hTree.avgDepth)


# max weight independant set
def C3W3_2():
	vertices = []
	i = -1
	with open('data/huffman.txt') as file:
		for line in file:
			i += 1
			if i == 0:
				continue
			vertices.append(int(line))
	w, A = MaxWeightIS(vertices)
	check = [1, 2, 3, 4, 17, 117, 517, 997]
	res = ''
	for v in check:
		res += str(w[v])
	print(res)


#  Snapsack
def C3W4_1():
	vertices = []
	i = -1
	with open('data/Knapsack1.txt') as file:
		for line in file:
			i += 1
			if i == 0:
				capacity = int(line.split()[0])
				continue
			vertices.append(tuple(map(int, line.split())))
	print('iterative', Knapsack(vertices, capacity))
	print('iterative2', Knapsack2(vertices, capacity))
	# print('recursive', Knapsack_r(vertices, capacity, len(vertices)-1))


#  Snapsack on bigger data set
def C3W4_2():
	vertices = []
	i = -1
	with open('data/Knapsack_big.txt') as file:
		for line in file:
			i += 1
			if i == 0:
				capacity = int(line.split()[0])
				continue
			vertices.append(tuple(map(int, line.split())))
	print(Knapsack2(vertices, capacity))


def test():
	vertices = [(3, 4), (2, 3), (4, 2), (4, 3)]
	print(Knapsack2(vertices, 6))
	print(Knapsack(vertices, 6))
	# print(res[len(vertices)][6])


if __name__ == '__main__':
	import sys
	import threading
	import time
	threading.stack_size(67108864)  # 64MB stack
	sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
	thread = threading.Thread(target=C3W4_1)  # instantiate thread object
	thread.start()  # run program at target
