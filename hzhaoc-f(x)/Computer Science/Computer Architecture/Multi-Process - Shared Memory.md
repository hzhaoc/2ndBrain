Multiprocessors can have shared or distributed memory. With a shared memory the programmer must ensure the processors cannot access the same memory location at the same time. Communication between processors is done through the shared memory. With distributed memory the processors must communicate through message passing.

##### Flynn’s Taxonomy of Parallel Machines
- SISD - Single Instruction, Single Data - typical single core processor
- SIMD - SIngle Instruction, Multiple Data - vector processor
- MISD - Multiple Instruction, Single Data - stream processor, not used very often
- **MIMD** - Multiple Instruction, Multiple Data - multi-processor

##### Why Multi-processors
Uniprocessors are preferable, but are limited by the frequency and instruction width.

##### Multiprocessor Needs Parallel Programs
Disadvantages of Multiprocessors:
- Parallel code is much harder to develop and debug. (lot of single threaded code)
- Performance Scaling is difficult to achieve

##### Centralized Shared Memory
UMA - Uniform Memory Access Time: All cores have caches, but share the main memory. Each core can share information by writing to the main memory. Also called Symmetric Multiprocessor ([[Task Scheduler#SMP|SMP]]). 
![[uniform mem access.png|600]]

- Problems with Centralized Main Memory
	- Memory needs to be large (and is therefore slow)
	- Memory get too many accesses/second
	- Memory bandwidth contention
	- Centralized Main Memory works only for small numbers of cores (<16)

##### Distributed Shared Memory
Non-Uniform Memory Access (NUMA): Each core will have its own cache and a slice of the main memory.
- pros
	- Each core will have fast access to its own slice of main memory
	- The memory bandwidth scales with the number of cores - more cores, more bandwidth.

With NUMA the operating system should put the **stack and data pages for core N in the memory slice associated with core N**. 

##### Distributed Memory
no sharing. each core has its own cache, memory, and a network interface card. A network message must be used for communicating between cores. This forces programmer to explicitly think about inter-core communication since it is exposed to them.
![[distributed mem.png|500]]

##### Share Mem vs Message Passing
see also [[Process#IPC]]

  &nbsp; | Message Passing | Shared Memory
------------ | ------------ | --------------
communication | programmer job | OS job
data distribution | programmer job | OS job
synchronization | none | programmer job
HW support | simple | extensive (MMU?)
programming correctness | difficult | less difficult
programming performance | difficult | very difficult

##### Shared Memory Hardware
Types of Shared Memory:
- Multiple cores share the same physical address space: [[Task Scheduler#SMP|SMP]] -> UMA, NUMA
- Multi-Threading by time sharing a core (does this mean no hardware support?)
- Hardware Multi-threading with coarse grain threading (change thread every few cycles), fine grain threading (change thread every cycle), or [[Thread#Hyper-threading|simultaneous multi-threading]] (SMT)
	- SMT is utilizing unused issue instruction slots in each cycle for multiple threads, which means multiple threads can issue instructions in same cycle or a core can execute multiple threads at the same time. It is even better than regular multi-threading. This is not much  more expensive than UMA or regular multi-threaded core.

##### SMT Hardware Changes
SMT is not much more expensive than a UMA or Fine Grained Multi-threaded core. For an SMT machine:
![[SMT hardware changes.png|500]]
- Add a program counter
- Add a RAT
- Add architectural registers

##### SMT with Data Cache, TLB
- With a VIVT Cache, SMT will lead to the wrong data being used because Cache does not do context switch on thread change.
- With a VIPT and a PIPT Cache the TLB must know which thread belongs to which processor. 
	- some CPUs flush TLB at process context switch; 
	- some better CPUs support ID (PCID/TID) tagged TLB for each entry. anyway, TLB are basically shared and manages V->P mappings for all processes.
	-  https://lwn.net/Articles/718204/
	-   https://cs.stackexchange.com/questions/94226/how-does-the-tlb-identify-a-particular-process
	-   https://stackoverflow.com/questions/34437371/is-the-tlb-shared-between-multiple-cores

##### SMT and Cache Performance
The cache is shared by all the SMT threads.
- benefit is data sharing.
- downside is possible cache size not enough for multithreads. Benefits of data sharing may be offset by increased cache miss if data shared is small.