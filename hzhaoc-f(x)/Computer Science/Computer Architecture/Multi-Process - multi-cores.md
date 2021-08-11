A discussion of the challenges encountered in implementing a multi-core system.

### challenge summary
![[multicore challenge.png|600]]

### Many Core Challenge 1
 on-chip traffic, or coherence traffic increases to the point of being a bottleneck
##### Network on Chip
1. Instead of a bus, use a mesh connection (displayed below). This will increase the throughput of the entire network.With a mesh, each additional core increases the number of connections to the network.Torus Networks are a wrapped mesh network.
![[mesh-network on chip.png|300]]
2. meanwhile, use directory based coherence implementation

### Many Core Challenge 2
**increased off-chip traffic** from more memory requests from more cache misses from more cores. note that number of pins/wires that connect to memory modules does not increase linearly to increased number of cores in a chip, which means off-chip traffic improvement is limited.

to solve this problem, use **Distributed Last Level Cache** (LLC)

##### Distributed LLC
- logically one shared cache
- but sliced up so each core gets part of it

![[distributed LLC.png|450]]

how to SLICE the cache?
- round robin by cache index. use last several digits of binary address of block to index core, say for 4-core chip, `00` to core 0, `01` to core 1, `10` to core 2, `11` to core 3. 
	- not good for locality
- round robin by page number. better locality

### Many Core Challenges 3
The Coherence Directory becomes too large when there are many cores.
##### On-Chip Directory
- The directory (home node) is sliced the same as the LLC.
- Partial Directory: 
	- a limited number of entries reserved for blocks that are in at least one **private** cache.
	- When a directory becomes full, use an LRU protocol to **replace** an entry. This type of miss is caused by **invalidation due to a replacement.**. Note this is another [[Mem Hier. Desi. - cache, mem, storage#Cache miss categories|miss category]] different from Compulsory, Capacity, Conflict, Coherence. 
		- When the old directory entry is being replaced, it sends invalidation request to all caches that has 1 presence bit of that block entry. Now all bits are 0 and it can be removed.

> There are a number of other obscure sources of misses that are not really worth naming - they occur very rarely compared to others. For example, 
> - the "cache was flushed because we changed the page table" kind of miss for virtually indexed caches
> - the "cache block was removed because the page was changed to uncacheable"
> 
> So the misses induced by directory entry replacements are not alone in being nameless. With a well-designed directory they happen relatively rarely. When they do occur, they are very similar to coherence misses in that the block's tag is present in the cache but the state of the block is Invalid. So when it is important to classify a miss into one of the four C categories, the "directory entry replaced" misses are counted as coherence misses. And they ARE caused by coherence (directory is there because of coherence, after all).

### Many Core Challenge 4
power split into cores. -> frequency & voltage in each core goes down, which slow down execution.

solution: frequency boost for single core.

### Many Core Challenge 5
The final challenge for Multi-cores is Operating system confusion caused by multi-threading and  cache sharing among cores.
##### SMT, Cores, Chips
The operating system needs to know on which core to run the thread to best utilize hardware resources (CPU, cache, etc.) and obtain the best performance