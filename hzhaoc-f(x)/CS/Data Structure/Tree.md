# Binary Search Tree
### Balanced Search Tree (BST)
- Descriptions:  trees that height of left leaves and right leaves are balanced (difference <=1)
- Advantages: fast in some operations (like insertion and deletion).
- Example: **Red Black Tree**
	- Property: 
		- Each node is read or black
		- Root is black
		- No two reads in a row (red node => only black children)
		- Every root-null path has same number of black nodes
	- Advantages: $O(logn)$  operations in insertion and deletion
	- Math Proof of tree balance: see [Stanford Algorithms from Coursera](https://www.coursera.org/specializations/algorithms)
	- Code: **to be added**
