## Descriptions: 
A type of priority queue. 
## Property: 
Parent is bigger than its children
## Advantages:
- Efficient data structure when dealing with min/max due to $O(logn)$ operations in insertion and popping (root/first element which is min  or max)
## Code Implementation
> also check [python heapq source code in Github](https://github.com/python/cpython/blob/main/Lib/heapq.py)
```python
class MinHeap:
	def heapify(self, array):
		"""Convert an random array into a heap."""
		for i in reversed(range(len(array) // 2)):
			self._siftdown(array, i)

	def pop(self, heap):
		"""Pop the smallest item off the heap, maintaining the heap invariant. """
		lastelt = heap.pop()  # raises appropriate IndexError if heap is empty
		if heap:
			returnitem = heap[0]
			heap[0] = lastelt
			self._siftdown(heap, 0)
			return returnitem
		return lastelt

	def add(self, heap, item):
		"""Add an new item into the heap, maintaining the heap invariant"""
		heap.append(item)
		self._siftup(heap, len(heap) - 1, 0)

	def addpop(self, heap, item):
		"""Add an new item, then pop and return the min or max item, more efficient than add() and then pop()"""
		if heap and heap[0] < item:
			item, heap[0] = heap[0], item
			self._siftdown(heap, 0)
		return item

	def popadd(self, heap, item):
		"""Pop and return min or max item, then add new item, more efficient than pop() and then add()"""
		returnitem = heap[0]  # raises appropriate IndexError if heap is empty
		heap[0] = item
		self._siftdown(heap, 0)
		return returnitem

	def _siftdown(self, heap, pos):
		"""
		Down-ward adjust an element's position in heap starting at pos, 
		(used to heap-down an element at start of heap to maintain heap property after pop)
		"""
		endpos = len(heap)
		startpos = pos
		newitem = heap[pos]
		childpos = 2 * pos + 1
		while childpos < endpos:
			rchildpos = childpos + 1
			if rchildpos < endpos and not heap[childpos] < heap[rchildpos]:
				childpos = rchildpos
			heap[pos] = heap[childpos]
			pos = childpos
			childpos = 2 * pos + 1
		heap[pos] = newitem
		self._siftup(heap, pos, startpos)

	def _siftup(self, heap, pos, startpos):
		"""
		Upward-adjust an alement's position starting at pos to startpos, 
		(used to heap-up an element at end of heap to start of heap to maintain heap property after insertion)
		"""
		newitem = heap[pos]
		while pos > startpos:
			parentpos = (pos - 1) // 2
			parent = heap[parentpos]
			if newitem < parent:
				heap[pos] = parent
				pos = parentpos
			else:
				break
		heap[pos] = newitem


class MaxHeap:
	def heapify(self, array):
		"""Convert an random array into a heap."""
		for i in reversed(range(len(array) // 2)):
			self._siftdown(array, i)

	def pop(self, heap):
		"""Pop the biggest item off the heap, maintaining the heap invariant. """
		lastelt = heap.pop()  # raises appropriate IndexError if heap is empty
		if heap:
			returnitem = heap[0]
			heap[0] = lastelt
			self._siftdown(heap, 0)
			return returnitem
		return lastelt

	def add(self, heap, item):
		"""Add an new item into the heap, maintaining the heap invariant"""
		heap.append(item)
		self._siftup(heap, len(heap) - 1, 0)

	def addpop(self, heap, item):
		"""Add an new item, then pop and return the min or max item, more efficient than add() and then pop()"""
		if heap and heap[0] < item:
			item, heap[0] = heap[0], item
			self._siftdown(heap, 0)
		return item

	def popadd(self, heap, item):
		"""Pop and return min or max item, then add new item, more efficient than pop() and then add()"""
		returnitem = heap[0]  # raises appropriate IndexError if heap is empty
		heap[0] = item
		self._siftdown(heap, 0)
		return returnitem

	def _siftdown(self, heap, pos):
		"""
		Down-ward adjust an element's position in heap starting at pos, 
		(used to heap-down an element at start of heap to maintain heap property after pop)
		"""
		endpos = len(heap)
		startpos = pos
		newitem = heap[pos]
		childpos = 2 * pos + 1
		while childpos < endpos:
			rchildpos = childpos + 1
			if rchildpos < endpos and not heap[childpos] > heap[rchildpos]:
				childpos = rchildpos
			heap[pos] = heap[childpos]
			pos = childpos
			childpos = 2 * pos + 1
		heap[pos] = newitem
		self._siftup(heap, pos, startpos)

	def _siftup(self, heap, pos, startpos):
		"""
		Upward-adjust an alement's position starting at pos to startpos, 
		(used to heap-up an element at end of heap to start of heap to maintain heap property after insertion)
		"""
		newitem = heap[pos]
		while pos > startpos:
			parentpos = (pos - 1) // 2
			parent = heap[parentpos]
			if newitem > parent:
				heap[pos] = parent
				pos = parentpos
			else:
				break
		heap[pos] = newitem
```
## Applications
- Median Maintain, see [Github code](https://github.com/hzhaoc/utils/tree/main/algo/medianmaintain.py)
- [[Huffman Codes]]
- compute [[Shortest Path]] in a graph between two vertexes. 
- compute Minimum Spanning Tree (Prim’s Algorithm), see [Github code](https://github.com/hzhaoc/utils/tree/main/algo/greedy.py)
