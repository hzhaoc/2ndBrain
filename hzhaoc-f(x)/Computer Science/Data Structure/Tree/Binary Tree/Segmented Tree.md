Useful for ranged sums. 

class implementation, 1D array
```python
class Node:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.v = None
        self.left = None
        self.right = None


class NumArray:
    def __init__(self, nums: List[int]):
        def _create(node):
            if node.l == node.r:
                node.v = nums[node.l]
            else:
                m = (node.l + node.r) // 2
                node.left = _create(Node(node.l, m))
                node.right = _create(Node(m+1, node.r))
                node.v = node.left.v + node.right.v
            return node
            
        self.root = _create(Node(0, len(nums)-1))
        
    def update(self, i, v):
        def _updt(node, i, v):
            if node.l == node.r:
                node.v = v
                return v
            
            m = (node.l + node.r) // 2
            if m >= i:
            	_updt(node.left, i, v)
            else:
                _updt(node.right, i, v)
                
            node.v = node.left.v + node.right.v
        
        _updt(self.root, i, v)
        
    def sumRange(self, l, r):
        def _range(node, l, r):
            if node.l == l and node.r == r:
                return node.v
            
            m = (node.l + node.r) // 2
            if m >= r:
                return _range(node.left, l, r)
            elif m < l:
                return _range(node.right, l, r)
            else:
                return _range(node.left, l, m) + _range(node.right, m+1, r)

        return _range(self.root, l, r)
```

list implementation, 1D array
```python
class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * self.n + nums  # segmented tree of size 2n
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]
        
    def update(self, i, v):
        i += self.n
        d = v - self.tree[i]
        while i:
            self.tree[i] += d
            i >>= 1
        
    def sumRange(self, l, r):
        l += self.n
        r += self.n
        res = 0
        while l <= r:
            if l & 1:
                res += self.tree[l]
                l += 1
            l >>= 1
            if not (r & 1):
                res += self.tree[r]
                r -= 1
            r >>= 1
        return res
```