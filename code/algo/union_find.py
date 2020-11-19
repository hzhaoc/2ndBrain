import warnings


class UnionFind:
	"""
	Lazy Union: In union(x, y) function, link x's root's parent to y's root
	total work of m finds (m is # of edges) = O(m* alpha(n))
	"""

	def __init__(self, vertexes):
		"""init union find object from list of numbered vertexes"""
		self._vertexes = vertexes
		self._parents = {x: x for x in self._vertexes}
		self._ranks = {x: 1 for x in self._vertexes}
		self._n_of_union = len(vertexes)

	@classmethod
	def _initfromGraph(cls, graph):
		"""init union find object from class of grpah"""
		return cls(graph.vertexes)

	def find(self, x):
		# optimize by Path Compression
		x_parent = self._parents[x]
		if x_parent == x:
			return x
		self._parents[x] = self.find(x_parent)
		return self._parents[x]

	def union(self, x, y):
		# optimize by Union by Rank
		x_root = self.find(x)
		y_root = self.find(y)
		if x_root == y_root:
			warnings.warn('{}, {} already in same union'.format(x, y))
			return
		self._n_of_union -= 1  # union makes number of unions decrease by 1
		x_rank = self._ranks[x_root]
		y_rank = self._ranks[y_root]
		if x_rank > y_rank:  # link y's root's parent to x's root
			self._parents[y_root] = x_root
		elif x_rank < y_rank:  # do opposite
			self._parents[x_root] = y_root
		elif x_rank == y_rank:  # arbitrarily do same as x_rank > y_rank, additionally add 1 to x's root's rank
			self._parents[y_root] = x_root
			self._ranks[x_root] += 1

	def inSameUnion(self, x, y):
		# check if x and y belongs to same union
		return self.find(x) == self.find(y)

	@property
	def parents(self):
		return self._parents
	
	@property
	def ranks(self):
		return self._ranks
	
	@property
	def vertexes(self):
		return self._vertexes

	@property
	def n_of_union(self):
		return self._n_of_union

	
	
