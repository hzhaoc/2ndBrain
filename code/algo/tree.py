import copy
from heap import MinHeap


class Node:
	def __init__(self, value=None, left=None, right=None):
		self._value = value
		self._left = left
		self._right = right

	def Depth(self):
		return

	def Depth(self):
		return

	def Root(self):
		return

	@property
	def value(self):
		return self._value
	
	@property
	def left(self):
		return self._left
	
	@property
	def right(self):
		return self._right


class HuffmanNode(Node):
	def __init__(self, value=None, left=None, right=None):
		super().__init__(value, left, right)


class HuffmanTree:
	def __init__(self):
		self._root, self._codes = None, None
		self._maxDepth, self._minDepth, self._avgDepth = 0, 0, 0

	def encode(self, symbols=None):
		"""
		Huffman-encoding symbols
		symbols: [(w1, s1), (w2, s2), ..., (wn, sn)] where wi, si are ith symbol's weight/freq 
		"""
		pq = MinHeap()
		symbols = copy.deepcopy(symbols)
		symbols = [(s[0], HuffmanNode(value=s[1], left=None, right=None)) for s in symbols]  # initialize symbols to nodes
		pq.heapify(symbols)
		while len(symbols) > 1:
			l, r = pq.pop(symbols), pq.pop(symbols)
			lw, ls, rw, rs = l[0], l[1], r[0], r[1]  # left weight, left symbol, right wreight, right symbol
			parent = HuffmanNode(value=None, left=ls, right=rs)
			pq.add(heap=symbols, item=(lw+rw, parent))
		self._root = pq.pop(symbols)[1]  # tree is complete, pop root node
		self._symbol2codes()  # create symbol: code dictionary
		self._maxDepth = len(max(self._codes.values(), key=len))  # max depth
		self._minDepth = len(min(self._codes.values(), key=len))  # min depth
		self._avgDepth = sum([len(d) for d in self._codes.values()]) / len(self._codes)  # mean depth

	@property
	def root(self):
		return self._root

	@property
	def codes(self):
		return self._codes

	def _symbol2codes(self):
		self._codes = dict()
		self._getCodes(self._root, '')

	def _getCodes(self, node, code):
		if not node.right and not node.left:
			self._codes[node.value] = code
			return
		self._getCodes(node.left, code+'0')
		self._getCodes(node.right, code+'1')

	@property
	def maxDepth(self):
		return self._maxDepth

	@property
	def minDepth(self):
		return self._minDepth

	@property
	def avgDepth(self):
		return self._avgDepth