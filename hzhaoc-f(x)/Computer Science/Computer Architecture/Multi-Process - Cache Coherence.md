This lesson discusses the problems and solutions for coherence. Different coherence protocols are discussed, including: MSI, MOSI, MOESI, and Directory. Each has advantages and disadvantages depending upon the **program being executed** and the **number of cores** in the system.

##### Cache Coherence Problem
The programmer expects to see shared memory. Problem is each core has its own cache as fast copy from shared memory. So the objective is to let all caches to be **coherent**. 

##### Coherence Definition
3 requirements:
1. If a core reads a memory location, the data received was written by the last valid write.
2. If a core writes to a memory location meanwhile another core reads that same memory location, it should see the **same value**. Any core should be able to read the last valid write to a memory location.
3. All cores should agree on the order of the writes to a memory location.

##### How to Get Coherence
- Don’t do caches. The main memory will be coherent : This leads to poor performance
- All cores share the same L1 cache. This leads to poor performance
- Use private write through caches. This is not coherent
- To maintain property 2:
	- **write-update**. cache write in one core are put on a shared bus which broadcast to other cores' caches
	- **write-invalidate**. cache write in one core make same data in other cores' caches **invalid**
- To maintain property 3:
	- **snooping**. all writes are shared on a bus and everybody snoops the bus
	- **directory bus**. each block state is maintained by a directory. When a write occurs the directory reflects the state change.

### Write-Update Snooping Coherence
Cores snoop shared bus to check incoming new writes from other cores. When a write is detected, any other copies of the block are updated by the new data. If there are two writes to the bus, an arbitrary decision is made on the order to the bus.
![[write-update snooping cache coherence.png|600]]
##### write-update optimization
- reduce memory writes
add **dirty bit** to each block and write back to mem when replaced. before replacement, when there's a write in core A, update cache in A and mark it as dirty; another core B snoops the dirty block in A and update in its own cache. this way, write to memory only when dirty block is replaced. and read from memory only when a core snoops no dirty blocks from any other cores.
> The memory does need some way to differentiate between a normal write on the bus, and a write that the memory needs to pick up. Usually there is a single bit on the bus that can be set, telling the memory that it needs to snoopy the request and update the memory.
- reduce bus writes
add **shared bit** to each block and add a line to the bus. if core B snoops a block on bus that's shared in its own cache, mark shared bit = 1, and pull 1 of that block in the bus so other cores will snoop it as well. this way, non-shared write blocks will not go to shared bus.

### Write Invalidate Snooping Coherence
similar to Write Update Snooping Coherence, the difference is when there's a write on core A and it gets broadcast to core B, the relevant block on B gets invalidated. when there's a new write on core  B, it misses on its own cache, and hit in core A, update its own cache. 
- Disadvantage: there is a miss on all the readers when a core writes
- Advantage: if a core needs to update the same block two or more times, the reads and writes can be done locally after the first write.

##### Update Vs. Invalidate Coherence
- If an application has a burst of write to one address or different address in same block, invalidate is better.
- If one core writes and another core reads often - update is likely better

**All? modern processors use Invalidate**, mainly because of another reason: invalidate is better when a thread moves to another core. (if update method, every write will consume shared bus to update the old core cache. if invalidate method, only first write for each block will have bus traffic.)

##### MSI Coherence
This is an invalidation based protocol.

![[MSI Coherence Protocol.png|800]]

##### Cache to Cache transfers for dirty block
Cache to cache transfers occur when a cache (C1) owns the data (the block is in the ‘M’ state) and a read request for the data (C2) is detected on the bus. C1 must supply the data because it has the only valid copy of the data.
Possible methods to do this:
1. Abort and retry
Downside of this approach - there needs to be two memory latencies to get the data to the requester.
3. Intervention
The core that owns the data intervenes and tells the memory it will respond. An intervention signal must be added to the bus. Disadvantage of this method: hardware is more complex.

Modern processors use the Intervention method

##### Avoiding (partial) Memory Writes on Cache to Cache Transfers for clean/dirty block
When using the Intervention method, the memory needs to be written when there is a read of modified data. It would be better if the memory was only written when the block is kicked out the cache - the Owner would be a new block state that is responsible for responding to read requests and updating memory.

##### O State
The ‘O’ state is like the ‘S’ state except:
1. when a read is detected, the owner responds
2. write-back to memory when the block is replaced

MOSI is like MSI except:
1. when M snoops Read on bus, it moves to O without write back to memory.

- M = a core has modified the data and has the only valid copy of the data
- S = at least one core has the block in its cache, clean
- O = a core has modified the data, and has shared the modified data with at least one other core

##### MOSI inefficiency
There is still inefficiencies in MOSI. When going from a Shared state to a Modified state, the block must send invalidation request on shared bus. This adds latency. To eliminate this a new state is introduced, the Exclusive state.

##### E State
The exclusive state is used when a core is the only core that has a clean copy of the data. When a Invalid block sends out Read request on bus, receive data from memory instead of other cores, it moves to M state because it knows it is the only block in all cores. Then when there's a write to this E block, it directly moves to the ‘M’ state without sends out Invalid request on bus, saving latency.
![[MOESI E State.png|600]]
(red I means Invalidation request on bus; red M means cache miss)

check [MESI animation](https://www.scss.tcd.ie/Jeremy.Jones/vivio/caches/MESIHelp.htm) 

### Directory Based Coherence
Snooping downside: every request must be broadcast, which means there must be one bus. This leads to a bottleneck and snooping can be scalded to more than 8~16 processors.

##### Directory
- A directory is distributed across all cores based on block address. (like block index in cache, for example, for 16 core, check some 4 bits in block addr)
- Each core has its own ‘slice’. 
- Each slice serves a set of blocks, each with an entry. 
- Each block entry keeps track of which caches have the block, for valid states only.
	- 1 dirty bit for **possible** dirty data in present cache (such as, mark it  as dirty for E state because it can silently be modified)
	- 1 presence bit / cache: 0 for absent and 1 for present.

The directory communication requires an acknowledgement from the cores after a request.

##### Summary of Cache Coherence Protocols

States | Access Type | Invariant |
-------| --------------| ---------|
Modified | read, write | all other caches in I state |
Exclusive | read | all other caches in I state |
Owned | read | all other caches in I or S state |
Shared | read | all other caches in I, S or O state |
Invalid | - | - |


> Because directory has only 1 dirty bit but many bits for caches, the directory sees O state as equivalent to S state! The directory effectively behaves like we have MESI not MOESI. Because it cannot use the O state correctly, **when O State block in a core responds to an outside Read Request, it needs to UPDATE MEMORY**. Therefore many directory-based protocols do not use the O state. If Directory has to see O as O state this way, when directory gets a read read quest, dirty bit =1, there are possibly more than 1 caches present for the requested block, but the directory does not know which cache really has that dirty bit, unless there's one dirty bit per cache which is not cheap.

> -  Normally here is a slice of the L2 cache and there is a cache for directory entries. If we replace the directory entry for a block from the directory cache, we don't have a larger directory table in memory. What we do is invalidate all sharers so the entry becomes empty. Now the entry can go away without breaking coherence. When someone needs to access the block after that, they send a request to the home, and it sees that no directory entry belongs to this block. This means that there are no sharers so the home allocates a directory entry (by removing directory state of another block) and behaves normally. Some requests require both directory and L2 info for the block. For example, a read miss from a core needs to allocate an entry in the directory (to mark the core as a sharer) and also it needs to read the block from L2. With separate L2 and directory stuff, we can have hits in both, misses in both, or a miss in one and a hit in the other. Having a miss in directory and a miss in the L2 cache is not a problem for correctness - we allocate a directory entry, mark the requestor of the block as a sharer, then read the data from L2 and send it on its merry way. Similarly, a hit in the directory but miss in L2 is not a problem - we fetch data from memory, put the data in L2, mark the requestor as a sharer and send the data to the requestor. 
> -  However, if the directory information and the L2 cache line are combined (basically the L2 line has the directory info), every block in L2 has directory state and blocks that are not in L2 do not have directory state. Not having directory state is a problem if the block exists in any of the coherent caches. **So if we evict a block from L2 (and thus lose its directory state) we must first invalidate the block from L1 caches.** This is exactly what inclusion does - a block can't exist in L1 if it is also not in L2. In real processors we now have private L1 and L2 caches (each core has its own) which are kept coherent, and the L3 cache is the shared one. So the above discussion works the same way, it would just be L3 instead of L2.

### Cache Misses with Coherence
The three ‘C’s’ are now four:
- compulsory, conflict, capacity
- coherence

Two types of Coherence miss:
- true sharing: different cores access same data
- false sharing: different cores access different data but same block