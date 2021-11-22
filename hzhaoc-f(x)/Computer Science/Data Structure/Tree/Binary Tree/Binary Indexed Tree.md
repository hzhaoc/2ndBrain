### BIT/Fenwick Tree
**useful for ranged sum of array.**

1D array:
```python
class NumArray(object):
    def __init__(self, nums):
        self.n = len(nums)
        self.a, self.c = nums, [0] * (self.n + 1)
        for i in range(1, self.n+1):
            self.c[i] += nums[i-1]
            _ = i + (i & -i)
            if _ <= self.n:
                self.c[_] += self.c[i] 

    def update(self, i, val):
        d, self.a[i] = val - self.a[i], val
        i += 1
        while i <= self.n:
            self.c[i] += d
            i += (i & -i)

    def sumRange(self, i, j):
        return self.doSum(j+1, 0) - self.doSum(i, 0)
    
    def doSum(self, i, s):
        while i:
            s += self.c[i]
            i -= (i & -i)
        return s
```

2D array:
```python
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
		'''O(n^2) run time'''
        self.m, self.n = len(matrix[0]), len(matrix)
        self.Mat = matrix
		
        self.BIT = [ [matrix[j-1][i-1] if i>0 and j>0 else 0 for i in range(self.m+1)] for j in range(self.n+1)]
        for i in range(1, self.n+1):
            for j in range(1, self.m+1):
                k = j + (j & -j)
                if k <= self.m: 
                    self.BIT[i][k] += self.BIT[i][j]
                    
        for i in range(1, self.n+1):
            for j in range(1, self.m+1):
                k = i + (i & -i)
                if k <= self.n:
                    self.BIT[k][j] += self.BIT[i][j]

    def update(self, r: int, c: int, v: int) -> None:
        d = v - self.Mat[r][c]
        self.Mat[r][c] = v
        r += 1
        c += 1
        while r <= self.n:
            y = c
            while y <= self.m:
                self.BIT[r][y] += d
                y += (y & -y)
            r += (r & -r)

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.CornerSum(r2+1, c2+1, 0) - \
               self.CornerSum(r2+1, c1, 0) - \
               self.CornerSum(r1, c2+1, 0) + \
               self.CornerSum(r1, c1, 0)
    
    def CornerSum(self, r, c, s):
        while r:
            y = c
            while y:
                s += self.BIT[r][y]
                y -= (y & -y)
            r -= (r & -r)
        return s
```