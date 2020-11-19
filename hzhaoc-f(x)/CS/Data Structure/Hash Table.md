1. Definition
Hash Tables are a data structure of constant size whose indexes are hash values from keys through hash functions and are within a fixed range. 
> From [a tutorial](https://www.tutorialspoint.com/python_data_structure/python_hash_table.htm#:~:text=Hash%20tables%20are%20a%20type,key%20for%20the%20data%20value.): Hash tables are a type of data structure in which the **address** or the index value of the data element is generated from a hash function. That makes accessing the data faster as the index value behaves as a key for the data value. In other words Hash table stores key-value pairs but the key is generated through a hashing function. So the search and insertion function of a data element becomes much faster as the key values themselves become the index of the array which stores the data.

2. Load: Load of hash table = # of objects in hash table / # of slots of hash table

3. Advantages: $O(1)$  in insertion, deletion, lookups

4. Hash Function
- Setup
Universe set U, an arbitrary size of input (key)
- Goal
Maintain evolving set S << U (a fixed size of hash values from key through hash function)
- Solving collision by
	-	Separate chaining (make the hashed value a linked list)
	-	Open addressing (probing: linear probing, random probing, double hashing)
-	Example: python dict
Python Dictionary uses a hash table (extra memory space allocated) to store key, hash, values in different ‘slots’ (each slot with one set of hash, key, value) for the information in the dictionary. 
-	How Dictionary in Python works: (from Stack Overflow)
	1.	When a new dict is initialized: the table starts with 8 slots. (slot indice i = hash(key) & mask, where mask = PyDictMINSIZE - 1).
	2.	When new entry is added to the dict: insertion starts with slot indice I (i = hash(key) & mask, where mask = PyDictMINSIZE – 1). Then:
	3. If that slot is empty:  
	The entry is added to that slot i. 
	4. If that slot is occupied:
	Compiler (e.g. CPython compares the hash AND the key of the entry in the slot with hash AND key of the new entry to be inserted. If both match, then it thinks the new entry already exists and move on. If not, probing is started. 
	5. Probing is to search slots in hash table one by one until an empty slot is found to insert the new entry. CPython uses random probing which picks the next slot in a pseudo random order, and the new entry is added to the first empty slot found.
	6. When an entry is looked up in the dict: compiler starts with the slot i where i is the hash of key from the entry that’s going to be looked up. If hash and key don’t match, then random probes until a matched slot found. If all slots are exhausted and no match is found, return error.
	7. Dictionary will be resized if it is two-thirds full to avoid slowing down lookups. 
