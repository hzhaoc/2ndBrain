This lesson is a review of caches. Beginning with the structure of the cache itself, including **set associative** and **direct mapped caches**. Then the lesson discusses **replacement policies**, specifically the **LRU policy**. The final portion of the lesson covers **write policies**; write back, write through, write allocate, and no-write allocate.

Think of Cache as a book you borrow from memory & disk as a library.

> See [[Cache Optimization]] for cache optimization techniques

##### Locality Principal
Things that happened recently are likely to happen again.

##### Memory Preference
- **Temporal Locality**: If an address has been accessed recently, it will likely be accessed again.
- **Spatial Locality**: If an address has been accessed, it is likely addresses close to it will be accessed.

##### Cache Lookups
- Fast -> Small
- access
	- hit
	- miss

##### Cache Performance
- avg mem access time (AMAT)
	- **AMAT = hit time + miss rate X miss penalty**
	- miss penalty = miss time - hit time

In a well designed Cache, hit rate is close to 1.

##### Cache Size (2021)
Multi-leveled Caches:
- L1 
	- 16k-512k bytes (PC)
	- hit rate = 90%
	- hit time = 1-3 cycles

##### Cache Organization
- determine hit/miss:
whether requested data from mem is in cache or not.

- determine what to (not) store in cache
- block size
block Size = the amount of data stored for each memory address. The block size should **at least be as large as the single largest access** that can be done in the cache. Usually 32 * 128 bytes work well for a block size. Choose a block size that is not too small to have no spatial locality, not too large to fit too few lines/blocks, and be power of 2 to match cache size

- block align
blocks should not overlap. and **blocks are aligned**. this means that cache cannot store any 64 byte (assume 64 byte) block from memory. it needs to be in form of 0-63, 64-127, this would make offset consistent with indexing byte in the block.

- Blocks in mem & cache
Memory has blocks of data and caches have lines of data. 

# Cache Mechanism
### Type
A cache can be thought of an abstract data table where each line can fit a block from memory. 
##### Direct Mapped Cache
- A block can only go to a specific line in the cache.
	- Pros: only one line to check hit/miss, fast. cheap. energy efficient. 
	- Cons: one specific block can only be put into one line, less efficient use of cache, lower hit rate; long LRU bits because the whole cache is one single set to reorder LRU bits for each cache access, which is high computing cost and high energy cost.
##### Set-Associative Cache
- A block can be placed in **N** number of lines in the cache, where **N** is one **sets**, and there are **(line # / N)** number of set in cache. It's called **N-way set associative**. Fully  Assoc &  Direct Mapped are 2 extreme examples of Set Assoc.
##### Fully Associative Cache
- A block can be placed in any line in the cache.
	- pro: more flexible/efficient use of cache, higher hit rate
	- con: long index bits, expensive block check

### Structure
![[cache struct.jpg|600]]
Above is an example of 2-way assoc with 4 sets in cache. 
- ##### data
actual data written from mem or CPU (if write-alloc)
- ##### index **(not physically in cache, just for explain in graph)**
index bits to index set number. here 4 sets needs **2 bits** for index. For a Direct Mapped cache, index bit length = 0 or no index because a block can be mapped to any line, so block number = tag; for a Fully Associative cache, index bit length = $log_2^N$ where $N$ is line #.
- ##### tag & block number
**block number** is the **tag & index** **together**. index is the LSB (least significant bits) of block number to index set number, and **tag is the remaining block number to index the specific block in that set.**.
- ##### offset **(not physically in cache, just for explain in graph)**
once a block is matched from tag + index, offset bits locates the exact byte in the block requested from professor. for example, offset `0100` maps to the 4th byte in the block needed for professor. **(tag + index + offset) bits may be the mem addr for the byte data requested (or there's `00` LSB not in offset because of word-align)**
- ##### valid bit
1 bit to indicate whether the data in this block/line is valid. usually when a program starts, all initial valid bits are set to 0. as soon as they get used, it changes to 1.
- ##### dirty bit
1 bit to indicate **whether the data in this block/line is written from memory or processor**. `0` means clean/from mem; `1` is dirty/from processor. if from processor, there'll be a policy how it will be written to memory.
- #### LRU bits (for replacement policy)
for example, suppose a 8-way associative cache, so LRU bits range from `000` to `111` per set. When CPU requests data block X to the cache and **hit** some block in a set, **the original bits where the block is put change to highest** `111` indicating newest, and **other original bits in the same set higher than the original bits where the block is put decrement by 1**. Later when a new block request is reached and **miss** this time, the oldest `000` LRU bits indicated block is kicked out to leave room for the missed data to be written into from memory. after replacement, do the reordering of LRU bits again. LRU methods is hardware expensive.

### Cache Replacement
data replacement in cache occurs when a set is full & data data so CPU needs to put new block in the set for the requested data. So which original block in the set to kick out?
- **random**
- **FIFO**: replace new with oldest
- **LRU**: replace new with least recently used. 
	- **NMRU**: because LRU is not that easy to implement, sometimes _randomly replace new with one of the not-most recently used._

### Write Policy
1. do we insert blocks we write?
- ##### write-allocate
modern caches are mostly this type (2021)
- ##### no-write-allocate

2. how do we synchronize cache and mem when write to cache?
- ##### write-through
write to cache and immediately write to mem
- ##### write-back
only write to mem when the block is being replaced. this is **most popular** (2021). usually paired with write-allocate.

### Cache Hierarchies
Different level caches are used to reduce the AMAT. If there is a miss in the first level cache, a second level cache is checked. If this level is a hit,then the time spent going to main memory is saved.

> AMAT = L1 hit time + L1 miss rate X L1 miss penalty
> L1 miss penalty = L2 hit time + L2 miss rate X L2 miss penalty
> L2 miss penalty = L3 hit time + L3 miss rate X L3 miss penalty
> ...

> Li latency < Li+1 latency
> Li capacity < Li+1 capacity

The equations will continue until the L# miss penalty = the main memory latency. This is called the Last Level Cache (LLC). Having a cache is better than no cache, and having a 2 level cache is better than having alone level cache.

##### local/global hit rate
- Local hit = a hit to an individual cache. For example a local hit for the L2 cache is a hit in the L2 cache. So L2 local hit rate may be low like 75%, but when we talk about L2 global hit rate which is when all accesses first try to access L2, it can be high as 97.5%.
- Global hit = the hits to all the caches.

> Global Hit Rate = 1 - Global Miss Rate
> Global Miss Rate = # of Misses in this cache / # of **all memory accesses**
> Local Hit Rate = # of Hits / # of Access **to this cache**
> MPKI = Misses per 1000 instructions

##### inclusion property
There are 3 different possibilities for the same block being in L1 and L2:
- A block in L1 may or may not be in L2
- A block in L1 must be in L2 (Inclusion)
- A block in L1 must NOT also be in L2 (Exclusion)

To enforce inclusion an inclusion bit is required. The bit will track if a block is in the other level caches.

> why inclusion helpful?
> 
> Inclusion makes several things simpler. When doing a write-back from L1, for example, inclusion ensures that the write-back is a L2 hit. Why is this useful? Well, it limits how much buffering we need and how complicated things will be. If the L1 cache is write-through, inclusion ensures that a write that is a L1 hit will actually happen in L2 (not be an L2 miss). And for coherence with private L1 and L2 caches (a la Intel's i3/i5/i7), inclusion allows the L2 cache to filter requests from other processors. With inclusion, if the request from another processor does not match anything in our L2, we know we don't have that block. Without inclusion, even if the block does not match in L2, we still need to probe in the L1 because it might be there.

### Cache Miss Category
causes of miss, 4 Cs: (see also [[Mem Hier. Desi. - cache, mem, storage#Cache miss categories|miss category]])
- **compulsory miss**: first time access. (the very first access to a block cannot be in cache. The block must be brought into cache from memory.)
- **capacity miss**: limited cache size. (limited number of blocks. Data requests need to further access memory.)
- **conflict miss**: limited associativity. (If a cache is not fully-associative (multiple sets), access to various blocks can be intermingled.)
- **coherence miss**: due to multi-core cache coherence implementation. (coherency misses are due to cache flushes to keep multiple caches coherent in a multiprocessor.)