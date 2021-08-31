# Merge Sort
idea is Divide and Conquer. (recursively split an array and merge two sub-arrays into one ordered array)
- **time: O(nlogn)**. (logn of divides * n of conquers per divide)
- **space: O(nlogn)**. (logn of divides, n length of array per divide)
- this is a [[Approaches#Divide and Conquer|divide and conquer]] algorithm
```python
def MergeSort(arr):
	"""
	idea is Divide and Conquer. (recursively split an array and merge two sub-arrays into one ordered array)
	time: O(nlogn). (logn of divides * n of conquers per divide)
	space: O(nlogn). (logn of divides, n length of array per divide)
	"""
	if not arr or len(arr) == 1:
		return arr

	lth = len(arr)
	left = arr[:lth // 2]
	right = arr[lth // 2:]

	left = MergeSort(left)
	right = MergeSort(right)

	newarr = []
	# use "pointer" or pop() to traverse array. pop() is a bit inconvenient since new array is created from start to end, but old array is deleted from end to start. 
	# Avoid use pop(0) because pop(0) is O(n) time
	# in my experiment with an array with length 500,000, pop() < pointer << pop(0)
	# I also tried collections.deque (double linked list), but it is bad for slicing
	while left and right:
		if left[-1] >= right[-1]:
			newarr.append(left.pop())
		else:
			newarr.append(right.pop())
	# use "x+=a", not "x=x+a" because "+=" calls __iadd__ which mutate object in place, and "=" create a new object and assign it to "x". 
	# see https://stackoverflow.com/questions/2347265/why-does-behave-unexpectedly-on-lists
	newarr += left[::-1]
	newarr += right[::-1]

	return newarr[::-1]
```

# Quick Sort
idea is Divide and Conquer. recursively split an array and partition an subarray by choosing a pivot element and ordering the array around the pivot so this particular pivot element is ordered in the correct position in the subarray. the choosing of the pivot element can be random, first, median, etc.
- **time: O(nlogn)**. (logn of divides * n of conquers per divide)
- **space: O(1)**. modify in place
- this is a [[Approaches#Divide and Conquer|divide and conquer]] algorithm
```python
def QuickSort(arr, l, r, pivot='random'):
	"""
	idea is Divide and Conquer.
	recursively split an array and partition an subarray by choosing a pivot element and ordering the array around the pivot so this particular pivot element is ordered in the correct position in the subarray
	the choosing of the pivot element can be random, first, median, etc.
	time: O(nlogn). (logn of divides * n of conquers per divide)
	space: O(1). modify in place
	"""
	if l < r:
		arr, pi = partition(arr, l, r, pivot=pivot)

		QuickSort(arr, l, pi - 1, pivot=pivot)
		QuickSort(arr, pi + 1, r, pivot=pivot)

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
		raise ValueError('pivot option {} is unavailable'.format(pivot))
	# partition array (use first item as pivot)
	pivot = arr[l]
	i = l
	for j in range(l + 1, r + 1):
		if arr[j] < pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[l], arr[i] = arr[i], arr[l]

	return arr, i
```

# Heap Sort
Turn an array into a [[Heap]], then the array can be easily reordered into a new array by keeping popping min arrays from the heap until it is done. 