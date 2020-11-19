from random import choice
import numpy as np
import random


def IntegerMulti(num1, num2):
	if not num1:
		return 0
	if not num2:
		return 0
	if len(str(num1)) == 1 and len(str(num2)) == 1:
		return num1 * num2

	l1, l2 = len(str(num1)), len(str(num2))
	if not not str(num1)[:l1 //2]:
		num1_1 = int(str(num1)[:l1 // 2])
	else:
		num1_1 = 0
	num1_2 = int(str(num1)[l1 // 2:])
	if not not str(num2)[:l2 // 2]:
		num2_1 = int(str(num2)[:l2 // 2])
	else:
		num2_1 = 0
	num2_2 = int(str(num2)[l2 // 2:])

	return 10**(l1 - l1 // 2 + l2 - l2 // 2) * IntegerMulti(num1_1, num2_1) + 10**(l1 - l1 // 2) * IntegerMulti(num1_1, num2_2) + 10**(l2 - l2 // 2) * IntegerMulti(num1_2, num2_1) + IntegerMulti(num1_2, num2_2)


def CountInversions(arr):
	if not arr or len(arr) == 1:
		return arr, 0
	lth = len(arr)
	left = arr[:lth // 2]
	right = arr[lth // 2:]

	left, count_left = CountInversions(left)
	right, count_right = CountInversions(right)

	newarr = list()
	count_split = 0
	while len(left) > 0 and len(right) > 0:
		if float(left[0]) <= float(right[0]):
			newarr.append(left.pop(0))
		else:
			newarr.append(right.pop(0))
			count_split += len(left)
	newarr += left
	newarr += right

	return newarr, count_split + count_left + count_right


def MergeSort(arr):
	if not arr or len(arr) == 1:
		return arr
	lth = len(arr)
	left = arr[:lth // 2]
	right = arr[lth // 2:]

	left = MergeSort(left)
	right = MergeSort(right)

	newarr = list()
	while len(left) > 0 and len(right) > 0:
		if left[0] <= right[0]:
			newarr.append(left.pop(0))
		else:
			newarr.append(right.pop(0))
	newarr += left
	newarr += right

	return newarr


def partition(arr, l, r, pivot):
	# choose pivot (exchange chosen pivot with first item)
	if pivot == 'random':
		_randIdx = random.choice(range(l, r+1))
		arr[l], arr[_randIdx] = arr[_randIdx], arr[l]
	elif pivot == 'first':
		pass 
	elif pivot == 'last':
		arr[l], arr[r] = arr[r], arr[l]
	elif pivot == 'median of three':
		if arr[l] >= arr[(l+r)//2]:
			if arr[l] >= arr[r]:
				if arr[(l+r)//2] >= arr[r]:
					arr[(l+r)//2], arr[l] = arr[l], arr[(l+r)//2]
				else:
					arr[r], arr[l] = arr[l], arr[r]
		else:
			if arr[l] < arr[r]:
				if arr[(l+r)//2] >= arr[r]:
					arr[r], arr[l] = arr[l], arr[r]
				else:
					arr[(l+r)//2], arr[l] = arr[l], arr[(l+r)//2]
	else:
		raise ValueError('pivot option {} is unavaiable'.format(pivot))
	# partition array (use first item as pivot)
	pivot = arr[l]
	i = l
	for j in range(l + 1, r + 1):
		if arr[j] < pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[l], arr[i] = arr[i], arr[l]

	return arr, i


def QuickSort(arr, l, r, pivot='random'):
	'''initial l, r values for partition are first index of array (0), last index of array (len(arr)-1)'''
	if l >= r:
		return arr

	arr, pi = partition(arr, l, r, pivot=pivot)

	arr = QuickSort(arr, l, pi - 1, pivot=pivot)
	arr = QuickSort(arr, pi + 1, r, pivot=pivot)

	return arr


def KargerMinCut(dic):
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
	# 1. combien vertix i and vertix j
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
