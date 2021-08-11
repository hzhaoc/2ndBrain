### Concept
Hash Tables are a data structure of constant size whose indexes are within a fixed range and are hash values from hash functions with element as input. The more evenly distributed the hash values are, the more efficient the hash table can be.
> From [a tutorial](https://www.tutorialspoint.com/python_data_structure/python_hash_table.htm#:~:text=Hash%20tables%20are%20a%20type,key%20for%20the%20data%20value.): Hash tables are a type of data structure in which the **address** or the index value of the data element is generated from a hash function. That makes accessing the data faster as the index value behaves as a key for the data value. In other words **Hash table stores key-value pairs but the key is generated through a hashing function**. So the search and insertion function of a data element becomes much faster as the key values themselves become the index of the array which stores the data.

- Load
Load of hash table = # of objects in hash table / # of slots of hash table

- Advantages: $O(1)$  in **insertion**, **deletion**, **lookup**

### Hash Function
- Setup
Universe set U, an arbitrary size of input (key)

- Goal
Maintain evolving set S << U (a fixed size of hash values from key through hash function)

- Solving collision by
	-	**chaining** (make the hashed value a linked list)
	-	**probing**:
		-	linear probing
			-	as example shown below, with linear probing, if original hash function without probing is $h(x)$, with probing, hash function can become $h'(x)=[h(x)+f(i)]$ where $f(i)=i$ (what linear means in name), $i=0,1,...$  (selected in order, should have a cap **?** ). this way, in insertion, if there's collision when $i=0$, do `i++` and rehash until no collision; in search, search element from $i=0$, if not found, `i++` and rehash until element found (**or all $i$ is traversed?**). Time Complexity of Insertion and Search in this probing will be **O(K) where k is maximum i.**
			-	each i in hash function also needs to be stored per entry to compare hashed keys AND hashes themselves. 
			-	linear probing might make elements clustered in a table. to avoid this, may use following: quadratic, random, double hashing, etc..
			-	![[hashing linear probing.png|500]]
		-	quadratic probing
		-	random probing
		-	double hashing
		-	etc..

##### Example: python dict
Python Dictionary uses a hash table (extra memory space allocated) to store hashed keys, hashes, values in different ‘slots’ (each slot with one set of hash, hashed key, value) for the information in the dictionary. 

How Dictionary in Python works: (from Stack Overflow)
- initialization
the table starts with 8 slots. (slot indice i = hash(key) & mask, where mask = PyDictMINSIZE - 1).

- insertion
	1. insertion of new pair {Key, Value} starts with slot indice i (i = hash(key) & mask, where mask = PyDictMINSIZE – 1). Then:
		- If that slot is empty: The entry {hash, hashed Key, Value} is added to that slot i. Finish.
		- If that slot is occupied: Compiler (e.g. CPython) compares: **old hash == new hash AND new hashed key == old hashed key**.
			- If true, new entry already exists. Update Value and hash. Finish. 
			- If false, start probing.
	2. Probing basically searches slots in hash table one by one until an empty slot is found to insert the new entry (**hash keeps changing during probing, that's why we need to store hash per entry**). CPython uses **random probing** which picks the next slot in a pseudo random order, and the new entry is added to the first empty slot found.

- search
	1. When an entry {Key Value} is looked up in the dict: compiler starts with the slot i where i is the hash of key from the entry that’s going to be looked up. If hash and key don’t match, then random probes until a matched slot found or the **limited (or all slots?)** probing completes. 
		- If matched slot found: return True.
		- If all slots are exhausted and no match is found: return False.

- resizing
Dictionary will be resized if it is two-thirds full to avoid slowing down lookups. 

##### Example: python Set
Like dict, set in python also implements hashing under the hood. Difference is Set does not need to stored hashed keys, it only needs to store hash and value, and the slot indice = hash(value)