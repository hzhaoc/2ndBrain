def C2W3():
	"""Median Maintain"""
	from heap import MinHeap, MaxHeap
	MinHeap = MinHeap()
	MaxHeap = MaxHeap()
	medians = []
	heaplow, heaphigh = [], []
	lowmax, highmin = float('-inf'), float('inf')
	with open('Median.txt') as file:
		for line in file:
			item = int(line)
			lenlow, lenhigh = len(heaplow), len(heaphigh)
			while True:
				if lenlow > lenhigh:
					if item >= lowmax:
						MinHeap.add(heaphigh, item)
						highmin = heaphigh[0]
						break
					if item < lowmax:
						returnitem = MaxHeap.popadd(heaplow, item)
						MinHeap.add(heaphigh, returnitem)
						lowmax = heaplow[0]
						highmin = heaphigh[0]
						break
				if lenlow <= lenhigh:
					if item <= highmin:
						MaxHeap.add(heaplow, item)
						lowmax = heaplow[0]
						break
					if item > highmin:
						returnitem = MinHeap.popadd(heaphigh, item)
						MaxHeap.add(heaplow, returnitem)
						lowmax = heaplow[0]
						highmin = heaphigh[0]
						break
			medians.append(lowmax)
			print('item', item, 'lowmax', lowmax, 'highmin', highmin)
	return sum(medians), len(medians)


if __name__ == '__main__':
	res, count = C2W3()
	print('sum', res, 'count', count, 'res', res % count)