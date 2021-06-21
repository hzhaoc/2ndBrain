# Overview
![[mem_hierarchy.png]]

- The gap between CPU memory demand (# requests / second) & DRAM bandwidth was growing. This effect is called **memory wall**. Recently the gap growth slowed down due to limited performance growth of a single processor. However, the gap between high-end multiprocessors memory demand  & DRAM bandwidth continues to grow. 
- Traditionally, designers focused on optimizing **average memory access time (AMAT)**, determined by **cache access time**, **miss rate**,  **miss  penalty**; More recently, **Power** is a major consideration. In some PMD cases, caches can account for 25% to 50% of the total power consumption.

### Cache
> Check [[Cache]] note also for specifically concepts of cache structure.

In cache, data move by **block** (multiple words). Each block includes a **tag** to indicate which memory address it corresponds to. A key design decision is where blocks can be placed in a cache. The most popular scheme is *set associative*, where a set is a group of blocks in the cache. A block is first mapped onto a set, and then the block can be placed anywhere within that set. Finding a block consists of first mapping the block address to the set, and then searching the set to find the block. The set is chosen by the address of the data:
$$(block \ address)\ MOD \ (Number \ of \ sets \ in \ cache)$$

If there are *n* blocks, it is called *n-way set associative*. A *direct-mapped*  cache has just one block per set. A *fully-associative* cache has just one set.

Caching writes is a bit difficult. A  *write-through* cache updates item in cache and writes through to update the main memory. A *write-back* cache only updates copy in the cache, and when the block is to be replaced, it is copied back to memory. **Both methods require a *write buffer* to allow the cache to proceed as soon as the data are placed the buffer rather than wait for full latency to write the data into memory.**

Cache **miss** categories:
- *compulsory*: the very first access to a block cannot be in cache. The block must be brought into cache from memory.
- *Capacity*: limited number of blocks. Data requests need to further access memory.
- *Conflict*: If a cache is not fully-associative (multiple sets), access to various blocks can be intermingled.
- *Coherency*: coherency misses are due to cache flushes to keep multiple caches coherent in a multiprocessor.

**Average memory access time** = **Hit time** + **Miss Rate** (miss / memory reference) X **Miss penalty** (cycles)

Cache optimizations:
1. _Larger block size to reduce miss rate_. Larger block size reduce compulsory miss, increase miss penalty, reduce static power slightly (fewer tags), increase capacity & conflict misses.
2. _Bigger caches to reduce miss rate_. Drawback is potential longer hit time of the larger cache memory and higher cost and power.
3. _Higher associativity to reduce miss rate_. Reduce conflict misses. Cons are increasing hit time & power consumption.
4. _Multilevel Caches to reduce miss penalty_. 	Low level cache with low hit time, high level cache with high bandwidth closer to memory.
For a two-level cache L1 & L2: (age mem access time is ave access time per request)
$$avg\ mem\ access\ time = Hit\ Time_{L1} + Miss \ Rate_{L1} * (Hit\ Time_{L2} + Miss\ Rate_{L2}*Miss\ Penalty_{L2})$$
As we can see, cache miss penalty for some level is the avg mem access time per reference for the next cache level.
5. _Giving priority to read misses over writes to reduce miss penalty_.  A write buffer holds updated value copy and may incur [[ILP - Pipeline#data dependencies|read-after-write]] data hazards when a cache miss happens. One solution is to check write buffer on read miss, thus read priority over write. This reduces miss penalty & little effect on power.
6. _Avoid address translation during indexing of the cache to reduce hit time_. Cache must copy with virtual-physical address translation to access memory. A common optimization is use [[Mem Mgmt#Page tables|page offset]] (the part that is identical in both virtual & physical addresses) to index the cache. The advantages of using this virtual index/physical tag method removing [[Mem Mgmt#TLB|TLB]] outweighs system complications it introduced.

# Memory Technology & Optimizations
access time: time between when a read is requested and when the desired word arrives;
cycle time: minimum time between unrelated requests to memory.

### SRAM Technology
Static-random-access-memory. SRAM doesn't need to refresh/ write back data after being read, unlike DRAM. Thus access time is very close to cycle time.
On-chip caches use SRAMs. Organized with a width that matches block size of the cache. This allows an entire block to be read or written within a single cycle. The access time to the cache is proportional to the number of blocks in  the cache, whereas the energy consumption depends both on the number of bits in the cache (static power) and on the number of blocks (dynamic power). 

### DRAM Technology
To prevent loss of information as the charge in a cell leaks away, each bit must be "refreshed" periodically. All bits in a row can be refreshed by reading that row and  writing it back. Every DRAM in the memory system must access every row within a certain time window, such as 64ms. DRAM controllers include hardware to refresh DRAMs periodically. Designer try to keep time spent refreshing to less than 5% of the total time.
#### Inside a DRAM: SDRAM
Synchronous DRAM. 
- Designers added a **clock signal** to the DRAM interface so that repeated transfers would not bear the overhead to synchronize with the controller. 
- SDRAMs also allowed addition of a **burst transfer mode** where multiple transfers can occur without specifying a new column address.
- A new innovation in early 2000s: **double-data-rate** (DDR) which allows a DRAM to transfer data both on the rising and the falling edge of the memory clock, thereby doubling the peak data rate.
- SDRAMs introduced **banks** to help with power management, improve access time, and allow interleaved and overlapped accesses to different banks.
DRAMs are commonly soled on small boards called *dual inline memory modules* (DIMMs) that contain 4-16 DRAM chips and that are normally organized to be 8-byte wide for desktop and server systems.
#### Graphics Data RAMs
GDRAMs or GSDRAMs are a special class of DRAMs tailored for handling higher bandwidth of graphic process units. 
Differences from normal CPU DRAMs:
1. wider interface. 
2. higher maximum clock rate on the data pins. GDRAMs normally connect directly to GPU and attached by soldering them to the board, unlike DRAMs, which are normally arranged in an expandable array of DIMMs.
#### Packaging Innovation: Stacked or Embedded DRAMs
Newest innovation in 2017 in DRAMs is packaging. It places multiple DRAMs in a stacked or adjacent fashion embedded within the same package as the processor. Processor & RAM in same package enables lower latency & higher bandwidth. It is also called **high bandwidth memory (HBM)**.
![[DRAM stacking.jpg]]
One version is to place the DRAM die directly on the CPU die, using solder bump technology to connect them. Another way stacks only DRAMs and abuts them with the CPU in a single package using a substrate (interposer) containing the connections.
In some applications, it may be possible to internally package enough DRAM to satisfy the needs of the application.

### [[Memory & Storage#Flash Memory|Flash Memory]] Technology
Property:
- A type of EEPROM (electronically erasable programmable read only memory), which is normally read-only but can be erased.
- Holds content without any power.

Differences from DRAM:
- reads to Flash are sequential and read an entire page. Thus long delay at the first byte of access for a random address but supply remaining bytes at 40MiB/s. Much faster than magnetic disks & much slower than SDRAM.
- must be erased before overwritten.
- nonvolatile. It keeps contents even without electricity. Energy efficient.
- limit for number of times any block can be written, typically 100,000 at least. 
- Cheaper than SDRAM; more expansive than disks.
- Like DRAM, Flash chips include redundant blocks to allow chips with small number of defects to be used.

### Phase-Change Memory Technology
Ongoing area with active research. Typically uses a small heating element to change the state of a bulk substrate between its crystalline form and an amorphous form, which have different resistive properties. 

Promising! Compared to Flash, wider write-durability, higher write performance, lower latency, lower cost...

### Enhancing Dependability in Memory Systems
- **Hard errors**are errors that arise from a change in circuitry and are repeatable, occurred during fabrication & operational circuit change.
- **Soft errors** are errors in cell content change. They are dynamic.

In very large systems, possibility of a complete failure of a single memory chip becomes significant. Chipkill was introduced by IBM to solve this. It is now a requirement for the 50,000 - 100,000 servers in WSCs.

# 10 Advanced Cache Optimizations
Remember **Average memory access time** = **Hit time** + **Miss Rate** (miss / memory reference) X **Miss penalty** (cycles)
For details see _Chapter 2 Section 2.3, Computer Architecture, A quantitative Approach, 6 Edition, by John L. Hennessy, David A. Patterson_

#### 1. Small & Simple First-Level Caches to reduce hit time & power
Despite Energy and Access Time cost, high associativity is implemented in first-level cache since:
- longer hit time is not critical. many processors take at least 2 cycle to access cache
- it keeps TLB out. TLB delay is bigger.
- with multithreading, conflict miss increase. Associativity reduces it.

#### 2. Way Prediction to reduce hit time
Extra bits in cache to predict the way or block within set of the next cache access. If predictor of next cache block access is correct, fast hit time; if not, try another block with an additional latency of one extra clock cycle. 
- pros:
	- lower avg mem access time
- cons:
	- makes it difficult to pipeline cache accesses

#### 3. Pipelined Access & Multibanked Caches to increase bandwidth
Primarily used on L1 cache
-  pipeline instruction cache access
	-  higher clock cycle, increased latency
	-  increase pipeline stage, greater penalty on misprediction
-  handle multiple data cache access per cycle: multibanking
	-  divide cache into independent banks, each supporting an independent access.
	-  reduce power consumption

#### 4. Nonblocking Caches to increase cache bandwidth
allow data cache to continue supply cache hits during a miss, thus "hit under miss". 
pros:
- reduce effective miss penalty
cons:
- nontrivial to implement

#### 5. Critical Word First & Early Restart to reduce miss penalty
This is based on observation that processor normally needs just one word of the block at a time. It is an impatience strategy:  don't wait for the full  block to be loaded before sending requested word and restarting the processor
- critical word first: request missed word first from memory and send it to processor as soon as it arrives; let processor continue execution while filling rest of the block
- early restart: fetch words in normal order, as soon as the requested word of the block arrives, send it to processor and let processor continue execution.
Benefit designs with large cache blocks.

#### 6. Merging Write Buffer to reduce miss penalty
Recall write-through & write-back in cache technique rely on write buffers, and a buffer is usually a "table" with multiple entries where each entry store multiple word / bytes. Write-merging is write one entry at a time, rather than write one word at a time for that entry. I/O device registers are often mapped into physical address space.These I/O addresses cannot allow write merging because separate I/O registers may not act like an array of words in memory.

#### 7. Compiler Optimization to reduce miss rate
This one does not require hardware change. Some researches:
##### Loop Interchange
Reordering nested loops to improve spatial locality and maximize use of data in a cache block before discarded.
##### Blocking
Again when dealing with multiple arrays, instead of operating row by row or column by column, **blocked algorithm** operate on submatrices or blocks. The goal is to maximize accesses to the data loaded into the cache before the data can be replaced.

#### 8. Hardware Prefetching of Inst & Data to reduce miss penalty or miss rate
Instruction prefetch is frequently done in hardware outside of the cache. Typically, the processor fetches two blocks on a miss: the requested block and the next consecutive block. The requested block is placed in the instruction cache when it returns, and the prefetched block is placed in the **instruction stream buffer**. If the requested block is present in the buffer, the original cache request is canceled, the block is read from the buffer, and the next prefetch request is issued.

A similar approach can be applied to data accesses. 

When prefetch works well, little impact on power; when prefetched data are not used or useful data are displaced, very negative impact on power.

#### 9. Compiler-Controlled Prefetching to reduce miss penalty or miss rate
Instead of hardware prefetch, do this in compiler. 
- Register prefetch loads value into a register
- Cache prefetch loads data only into the cache and not the register.

#### 10. Use HBM to extend mem hierarchy
Use packaged DRAMs to build massive L4 cache, with upcoming technologies ranging from 128 MiB to 1GiB and more.

# Example: Intel Core i7 6700
See  _Chapter 2 Section 2.6 Computer Architecture, A quantitative Approach, 6 Edition, by John L. Hennessy, David A. Patterson_