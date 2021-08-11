advanced topic from [[Cache Basic]]

# Overview
recall cache performance measurement:
> AMAT = Hit time + Miss Rate * Miss Penalty

optimization goal:
- reduce hit time
- reduce miss rate
- reduce miss penalty
- increase bandwidth

optimization techniques summary:

approach | goal
------------ | ------------
reduce hit time | pipelined cache access
reduce hit time | small L1 cache
reduce hit time | VIPT cache (aliasing problem, way prediction)
reduce hit time | replacement policy (LRU, NMRU, PLRU)
reduce miss rate | larger cache block/line
reduce miss rate | prefetch blocks (hardware/compiler)
reduce miss rate | Loop interchange (compiler)
reduce miss rate | blocked algorithm (compiler)
reduce miss penalty | overlap misses with MSHR / non-blocking cache
reduce miss penalty | Critical Word First & Early Restart
reduce miss penalty | Merging Write Buffer
reduce miss penalty | multilevel cache
reduce miss penalty | read write buffer on read miss (read priority over write)
increase bandwidth | multibanked cache
extend hierarchy | [[Mem Hier. Desi. - cache, mem, storage#HBM]]


# Reduce hit time
- ~~reduce cache size (X, bad for miss rate)~~
- ~~reduce cache assoc (X, bad for miss rate)~~
- overlap cache hit w another hit: **cache pipeline**
- overlap cache hit w TLB hit: **VIPT cache (+ way prediction)**
- maintain replacement state more quickly: **NMRU**, **PLRU**

### pipelined caches
Primarily used on L1 cache. Execution of "cache access and if hit, reading or if not hit, do other" can be pipelined into several stages. indexing, tag compare to determine hit can be done before data reading for separation. L1 cache is usually 1-3 cycles. 2-3 cycle caches can be pipelined.
-  pros: higher clock frequency
-  cons: increased latency from greater penalty on misprediction

### VIPT cache
###### PIPT Cache
**physically-indexed physically-tagged** cache. it means index and tag are from **phys addr**. 

**latency in this case is TLB access + cache access**

![[PIPTCache.png|500]]

###### VIVT Cache
virtual-indexed virtually-tagged cache is **not viable**, because 1. cache still need read/write permission bits from TLB. 2. VM is per process. these create chaos in one cache.

##### VIPT cache
So **virtually-indexed physically-tagged** cache is introduced. 

Advantages: CPU does cache indexing, returning tags and TLB access, returning frame # concurrently. so latency is only **cache hit time mostly**.
![[VIPTCache.png|600]]

##### aliasing problem
- two virtual addr on two processes can map to same physical addr. TLB return same frame #. but virtual index bits are still different and may result into different tags to compare, and different results for these two virtual addr. 
- However, this is not a problem if cache is small enough. As long as index bits are within page offsets shown below, 2 different virtual addresses that map to same physical address would have same page offset which includes same index.
- From above, we can deduce that **Cache Size <= Assoc X Page Size**
	![[VIPTCache Aliasing issue.png|400]]

##### Way Prediction
Since VIPT cache has high associativity to increase cache size & reduce hit rate, down side is more tags to check and slower hit time. Improvement is first do a direct-map (with extra bits in cache) to predict which line in the set is mostly likely to hit, if not hit, then do normal set-assoc check as before (additional latency). 
- pros:
	- lower avg mem access time
- cons:
	- makes it difficult to pipeline cache accesses

### Replacement Policy
- Random: good hit time (nothing to do when cache hit), bad miss rate
- LRU: good miss rate. bad hit time (update LRU bits when cache hit)
- PLRU: a compromise between NMRU & LRU. medium performance & time overhead.
- NMRU: compared to LRU, no good performance, good hit time.

##### LRU replacement
for example, suppose a 8-way associative cache, so LRU bits range from `000` to `111` per set. When CPU requests data block X to the cache and **hit** some block in a set, **the original bits where the block is put change to highest** `111` indicating newest, and **other original bits in the same set higher than the original bits where the block is put decrement by 1**. Later when a new block request is reached and **miss** this time, the oldest `000` LRU bits indicated block is kicked out to leave room for the missed data to be written into from memory. after replacement, do the reordering of LRU bits again. LRU methods is hardware expensive.

> For low associativity, we can implement LRU using a state machine (no counters). E.g. The 2-way implementation has two states (one LRU bit) and is the same as NMRU. For 4-way, there are 24 (4!) states. A state here tells us everything the counters would, e.g. there is a state that says way 0 is the most recent, then way 1, then way 2, and then way 3. There is a state that says way 0 then way 1 then 3 and then way 2. Overall there are 24 states so 5 bits are enough (the counters would need 8 bits), and the logic for the state machine is manageable. But for 8-way we need 40320 (8!) states, which gives us only 16 bits (counters would need 24) **but the logic for updating and picking a replacement victim becomes very messy and slow**.

##### NMRU replacement
not most recently used. track which block is MRU and pick a non-MRU block on replacement.
- one MRU **pointer** per set (vs N LRU counter bits)
- works reasonably well

##### PLRU replacement
pseudo-LRU. one bit / line in set initialized at `0`. one access to one line sets the bit to `1` indicating recently used. remaining `0` bits are for non-MRU as replacement options. When the last `0` is set to `1`, all other `1` bits are set back to `0` indicating non-MRU. PLRU is a compromise between NMRU & LRU. medium performance & time overhead.

> finding the next bit that is zero would not be done by reading the bits one at a time - one would use specialized circuitry for that. Similarly, resetting of all the bits would not be done one at a time - we would use bulk-reset circuitry. In contrast, for LRU we would need to update counters. There are ways of making that a bit simpler, but it's still much more complicated than setting a bit and an occasional bulk reset. 
> 
> cost in PLRU is a bit per way in the set, not a counter per way. When associativity is high (8 or more) this makes PLRU a lot cheaper and more energy efficient.

Finally, note that the cost in PLRU is a bit per way in the set, not a counter per way. When associativity is high (8 or more) this makes PLRU a lot cheaper and more energy efficient.


# Reduce miss rate
### larger cache blocks
- more words brought in on a miss,  miss rate down with high spatial locality; low otherwise
- larger block size can reduce **compulsory**, **capacity** (due to spatial locality, think of accessing a large array), and **conflict misses** (same?).
- ![[miss rate and block size.png|400]]

### prefetching blocks
Prefetch blocks into the cache to improve the miss rate. Good guesses eliminate misses, while bad guesses cause cache pollution. (When prefetch works well, little impact on power; when prefetched data are not used or useful data are displaced, very negative impact on power.)

##### compiler prefetch inst
Compiler does inst sche and prefetch future inst to bring predicted future blocks in cache. The compiler can be used to determine which blocks to fetch. 
- Register prefetch loads value into a register
- Cache prefetch loads data only into the cache and not the register.

The question becomes:
>  how far in advance should the blocks be fetched?

This is a **difficult question to answer with a compiler**.

##### hardware prefetch inst
cache or processor guess what to be accessed soon. Instruction prefetch is frequently done in hardware outside of the cache.

A similar approach can be applied to data accesses. 
- **stream buffer**: prefetch next blocks in sequential.
	Typically, the processor fetches two blocks on a miss: the requested block and the next consecutive block. The requested block is placed in the instruction cache when it returns, and the prefetched block is placed in the **instruction stream buffer**. If the requested block is present in the buffer, the original cache request is canceled, the block is read from the buffer, and the next prefetch request is issued.
- **stride prefetcher**: prefetch the block at distance ‘d’
- **correlating prefetcher**: if A is fetched, then B should be prefetched, etc

### Loop interchange
compiler optimizations to change the code to have better locality by swapping the inner and outer loops to sequentially access the matrix in memory. For example as below.
![[loop interchange.png]]


# Reduce miss penalty
### Overlap Misses
Reducing the Miss Penalty can be accomplished by overlapping the misses. While the OOO processor is waiting for a cache miss,** it continues to execute instructions** so part of the load cache miss latency is hidden. Within these instructions, the processor may encounter another cache miss. This is an overlapping miss.

- **blocking cache**. Only one load at a time can be performed. If a cache gets a load instruction,no other load instruction can be executed until the first load is completed.
- **Non-blocking Cache**. A non-blocking cache will allow
	- _Hit-under-miss_. if the processor is waiting for a miss, it can execute cache hits
	- _miss-under-miss_. if the processor is waiting for a miss, it can execute additional requests to memory (other misses). it requires Memory-Level Parallelism support. This **largely overlap cache misses and reduce latency.**

##### Miss Under Miss Support in Caches
- **Miss Status Handling Registers (MSHR)**
	- keep information about misses that are in progress
	- when processor sends request, check MSHRs to see if the requested cache miss is one that has already been requested
		- if the cache miss is a new miss (a true miss):
			1. allocate an **MSHR register**
			2. track which instruction is waiting for the miss
		- if the cache miss has already been requested (a half-miss):
			1. the instruction is added to the MSHR
	- When data arrives from mem:
		- The MSHR is used to alert the correct instructions that their requested data is ready
		- Release the MSHR register

> How many MSHR registers are necessary? 
> 16 - 32 MSHR is a typical number

Applications that can benefit from the MSHR are those that have misses often enough so the next miss can be issued and executed before the processor runs out of resources while"stalling" on the previous miss.

# Increase bandwidth
#### Multibanked Caches
To increase bandwidth. Primarily used on L1 cache. Handle multiple data cache access per cycle
-  divide cache into independent banks, each supporting an independent access.
-  reduce power consumption


# Other
- For details see _Chapter 2 Section 2.3, Computer Architecture, A quantitative Approach, 6 Edition, by John L. Hennessy, David A. Patterson_

#### Small & Simple First-Level Caches to reduce hit time & power
Despite Energy and Access Time cost, high associativity is implemented in first-level cache since:
- longer hit time is not critical. many processors take at least 2 cycle to access cache
- it keeps TLB out. TLB delay is bigger.
- with multithreading, conflict miss increase. Associativity reduces it.

#### Critical Word First & Early Restart to reduce miss penalty
This is based on observation that processor normally needs just one word of the block at a time. It is an impatience strategy:  don't wait for the full block to be loaded before sending requested word and restarting the processor
- critical word first: request missed word first from memory and send it to processor as soon as it arrives; let processor continue execution while filling rest of the block
- early restart: fetch words in normal order, as soon as the requested word of the block arrives, send it to processor and let processor continue execution.
Benefit designs with large cache blocks.

#### Merging Write Buffer to reduce miss penalty
Recall write-through & write-back in cache technique rely on write buffers, and a buffer is usually a "table" with multiple entries where each entry store multiple word / bytes. Write-merging is write one entry at a time, rather than write one word at a time for that entry. I/O device registers are often mapped into physical address space. These I/O addresses cannot allow write merging because separate I/O registers may not act like an array of words in memory.

#### Compiler Optimization: Blocking to reduce miss rate
When dealing with multiple arrays, instead of operating row by row or column by column, **blocked algorithm** operate on submatrices or blocks. The goal is to maximize accesses to the data loaded into the cache before the data can be replaced.

#### use HBM to extend mem hierarchy
Use packaged DRAMs to build massive L4 cache, with upcoming technologies ranging from 128 MiB to 1GiB and more.

### read write buffer on read miss
_Giving priority to read misses over writes to reduce miss penalty_.  A write buffer holds updated value copy and may incur [[ILP - Pipeline#data dependencies|read-after-write]] data hazards when a cache miss happens. One solution is to check write buffer on read miss, thus read priority over write. This reduces miss penalty & little effect on power.

# Example: Intel Core i7 6700
See  _Chapter 2 Section 2.6 Computer Architecture, A quantitative Approach, 6 Edition, by John L. Hennessy, David A. Patterson_