def C2W4():
	"""two sum problem, utilizing hash table (set)"""
	data = set()
	with open('data\\2sum.txt') as file:
		for line in file:
			data.add(int(line))
	res = 0
	for i in range(-10000, 10001):
		res += twoSum(data, i)
		print(i, 'done')
	return res

def twoSum(data, target):
	for i in data:
		if target - i in data:
			return 1
	return 0


if __name__ == '__main__':
	res = C2W4()
	print(res)