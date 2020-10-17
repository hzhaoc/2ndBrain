# Concept
Binary codes are sequence of binary numbers $0, 1$ that encode human understandable information (characters, etc,) to electronic computers. Think of binary codes graphically as a path in a built binary tree, where leaves point to characters, and each paths to leaf is a binary code for that character.

For example, for the binary codes tree below, binary code for character $\mathbf{a}$ is $0011$. As a result, a list of characters can be represented by a sequence of their **prefix-free** binary codes. By prefix-free it means each character's binary code is a path to leaf, no internal node in the tree, so there's no conflict in prefixes of all binary codes.

```
								______0______
							   /             \
							__0__           __1__
						   /     \         /     \
						  0       1       0       1
						 / \     / \     / \     / \
						0   1   0   1   0   1   0   1
								   (a)
```
Source code (.py)
```
from binarytree import Node 

def generate_btree4encode(node, depth):
    # generate a binary tree of 0, 1 for encoding
    if depth==0:
        return
    node.left = Node(0)
    node.right = Node(1)
    generate_btree4encode(node.left, depth-1)
    generate_btree4encode(node.right, depth-1)

def main():
    root = Node(0)
    depth = 3
    generate_btree4encode(root, depth)
    print(root)

if __name__ == "__main__":
    main()
```

# Objective
In binary encoding, our objective is to use the shortest total or average length of binary numbers to encode a list of characters. Mathematically, for a list of characters $[s_1, s_2, ..., s_n]$, denote their frequency probability as $[p_1, p_2, ..., p_n]$, then our objective function is:
$$\min_{s,\;p}\; B(S,P)=\frac{1}{n}\sum_i^np_i*len(s_i)$$
where $len(s_i)$ denotes length of binary codes of $s_i$ 

# Solution

## Huffman Codes

### Theory
Huffman Codes algorithm first sorts a set of characters in a file or a string based on its frequency. Here a ascending-sorted set of $[p_1, p_2, ..., p_n]$ denotes corresponding frequency probability for a character set $s_1, s_2, ..., s_n$. 

Next, **merge** $s_1$ and $s_2$ which have the lowest frequencies among $S$ to a parent node $(s_{12})$ where its frequency is $p_1+p_2$.  Next, in the new character set $[s_12, s_3, ... s_n]$, do the merging step again. The merging step recursively goes on until there's one single node $s_{12...n}$ where its frequency is $1$. 

The structured binary tree from this bottom up approach is the optimal binary codes that minimizes our objective $B(S, P)$.

### Property
-	Leaves point to characters. Path is its binary code.
-	Depth of Huffman Codes binary tree = number of merges.
-	Length of a binary code in the tree for a character = number of merges it participated.
-	The longer the binary code, the lower frequency its represented character.

### Correctness Proof
Use **Mathematical Induction** method: assume number of characters in a set $n>=2$. When $n=2$,  obviously Huffman Codes is correct.

When $n\geq3$, we need to prove Huffman Codes is correct when $n=k+1$ if Huffman Codes is correct when $n=k$, $\forall{k}\in{(3,4,...,n)}$. If Huffman Codes is correct when $n=k$, when $n=k+1$, merge the $s_1$, $s_2$ with the lowest two frequencies to $s_12$, now the character set is $S((12),3,4,...n)$ and $n=k$. 

According to our assumption, when $n=k$, Huffman Codes tree $B(S_{12, 3,...,k}, P)$ is an optimal binary codes tree (that minimizes average binary code length). So we only need to prove: based on $B(S_{12, 3,...,k}, P)$ with $s_{12}$ is the merge of two lowest frequency character $s_1$, $s_2$, when $s_{12}$ is split into two child nodes $s_1$ and $s_2$, thus $n=k+1$, the binary codes tree is still optimal and it's still Huffman Codes.

```
								______0______
							   /             \
							  0             _..._
									       /     \
								          0       1 (s_12)
											     / \
											    0   1
											 (s_1)  (s_2)
```

To prove $B(S_{1, 2, 3,...,k}, P)$ is Huffman Codes, since $B(S_{12, 3,...,k}, P)$ is optimal Huffman Codes, we only need to prove $s_1$, $s_2$ are at the deepest of the tree. Assume they are not, then there are $s_i$, $s_j$ that are deeper and have lower frequencies. This violates the assumption $s_1$, $s_2$ are the ones with lowest frequency. Thus $B(S_{1, 2, 3,...,k}, P)$ is Huffman Codes.

To prove $B(S_{1, 2, 3,...,k}, P)$ is optimal binary codes tree, assume there exists $B^{'}(S_{1, 2, 3,...,k}, P)$ that makes $B^{'}<B$, and $s_1^{'}$, $s_2^{'}$ are not the two with lowest frequencies $p_1^{'}$, $p_2^{'}$, because  $B(S_{1, 2, 3,...,k}, P) = B(S_{12, 3,...,k}, P)+p_{1}+p_{2}\leq B(S_{12, 3,...,k}, P)+p_1^{'}+p_{2}^{'}=B^{'}(S_{1, 2, 3,...,k}, P)$, there's a better $B$ than $B^{'}$. Therefore assumption fails. $B(S_{1, 2, 3,...,k}, P)$ is optimal binary codes tree.

### Reference
-	[Coursera: Algorithm - Peking University](https://www.coursera.org/lecture/algorithms/058ha-fu-man-suan-fa-de-zheng-que-xing-zheng-ming-nLQya)
-	[Coursera: Greedy Algorithm - Stanford University](https://www.coursera.org/learn/algorithms-greedy)

# Application
## File Compression
Lossless. One of the best currently.

