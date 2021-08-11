Given an undirected and unweighted graph, find the smallest cut (smallest number of edges that disconnects the graph into two components).  The input graph may have parallel edges.

##### Karger's Minimum Cuts
Because it's random contract, result may not always be minimum number of cuts, 
so do it $n*n*logn + 1$ times,
Probability of returning a min cut $\approx\frac{1}{n^2}$
```python
def KargerMinCut(dic):
	"""
	Given an undirected and unweighted graph, find the smallest cut 
	(smallest number of edges that disconnects the graph into two components). 
	The input graph may have parallel edges.

	Because it's random contract, result may not always be minimum number of cuts, 
	so do it n*n*logn + 1 times,
	Probability of returning a min cut ~= 1/n^2

	@params
	: dic: dictionary of lists, keys are vertices and values are adjacent vertices
	"""
	res = []
	N = int(len(dic) * len(dic) * np.log(len(dic))) + 1
	for i in range(N):
		while len(dic) > 2:
			dic = RandomContract(dic)
		res.append(sum([len(v) for v in dic.values()]) / 2)
	return min(res)

def RandomContract(dic):
	"""
	dic: dictionary of lists, keys are vertices and values are adjacent vertices
	Probability of returning a min cut ~= 1/n^2 
	"""
	# choose random vertex
	i = choice(list(dic))
	# choose random adjacent vertex
	j = choice(dic[i])
	# contract edge i-j: 
	# 1. combine vertix i and vertix j
	temp = dic[i] + dic[j]
	# 2. delete self loops within vertix i and j
	temp = [x for x in temp if x != i and x != j]
	# 3. keep i, drop j
	dic[i] = temp
	del dic[j]
	# 3. unify i, j to same vertix, here i, in all other vertice' adjacent vertice
	for k, v in dic.items():
		if k == i or k == j:
			continue
		while j in v:
			v[v.index(j)] = i
		dic[k] = v
	return dic
```
