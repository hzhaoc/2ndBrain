B tree is a M-way search tree (a node with M maximum child nodes) with rules for creation & changing of the tree. 

##### why use B/B+ tree?
in a database system, data are stored in usually [[Storage Hierarchy#Hard Disk Drive|disks]] file system (2021) in blocks. In order to have quick access to some blocks, you need a quick lookup in the indexes where one index may check one data block in  disk. (a index/block address table with database keys). Index table is also stored in blocks in disk but will be smaller than original data table. This way, lookup in index table is faster than lookup in original data table. If the index table is still too large, use a second index table to lookup the first index table. Thus a multi-level indexing approach.  And this can be represented by a M-way search tree, like a B tree. 

##### B tree property
for a M-degree B tree (M-way search tree)
- each non-leaf node has min 2 children
- a node has M-1 data keys, M-1 data block pointers/start addresses, M child pointers.
- **bottom-up growth/build of tree** when a node is at least half full **(?)** (it has stored M keys) and there's a new one coming in, split the node using one intermediate key. the intermediate key levels up and becomes parent; the remaining keys which are smaller than this parent key become its left child node, and the ones no smaller than this parent key become its right child node. 
- leaf nodes are at same depth

example
![[dbms b tree.png|500]]

##### B+ tree property
B+ tree has similar properties of B tree. Difference between B tree and B+ tree is that:
- when a node is reaching some limit and start splitting, the one intermediate key which levels up one node keeps a copy in the child node. so now after splits, the two child nodes together has all the keys. this way, **leaf nodes has all keys, and internal nodes only need to store child pointers and keys (no more data pointers)**.
- leaf nodes are linked together

example
![[dbms b+ tree.png|500]]

##### B+ tree vs B tree
- B+ tree internal node size is smaller (it does not need to store data pointers as said), so a cache can store more B+ nodes, resulting in lower cache miss.
- B+ tree leaf nodes are inter-connected which makes ranged database query very efficient. 
- frequent access to some nodes can be faster in B tree (because internal nodes has data pointer, the searching does not necessarily need to go down to bottom).

###### note
recommend [this](https://www.youtube.com/watch?v=aZjYr87r1b8) youtube video.
