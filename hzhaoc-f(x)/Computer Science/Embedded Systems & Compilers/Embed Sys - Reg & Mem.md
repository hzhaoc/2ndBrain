Registers and memories are the most important part of computer architecture, especially for RISC processors. RISC processors require all data be in registers before execution of instructions.    

# Registers 
- architecturally visible containers other than memory
- register files: a homogeneous register set 

Superscalar or VLIW Parallel Function Architecture    
![[vliw parallel funct arch.png|600]]

Superscalar with bypassing:
![[parallel funct arch with bypassing.png|600]]  

In VLIW there is no bypassing. There are specific instructions for moving data from register to register, this gives more flexibility to the programmer, but it means there can be no bypassing.

##### Clustering
Traditionally, there were large multiported register files, but scalability was hindered by this method. In VLIW intercluster communication is necessary. There is also a memory interface unit. Most communication will be within the cluster, much less communication intercluster, and very little memory communication.    
![[register clustering.png|600]]
![[vliw clusters.gif]]
**Two Types of Clustering **
- Architecturally Invisible 
	- appears as one large register file to the compiler.
	- The hardware needs to copy between register files.
	- detecting when copies of data are needed is hard.
	- all the registers need to be exposed in one operand field, so there is a large operand field.
	- Hardware stalls due to copying between registers, which is invisible to the compiler.
	- This solution is NOT scalable. 
- Architecturally Visible Clustering
	- the ISA must include a way to specify operations assigned to each cluster.
	- The copies between clusters are implicit copy or explicit copy
	- Directly copy registers to registers in a different cluster 
		- **Implicit copy**: operations may r/w operands in nonlocal registers. But complicated for scheduling and scalability issues. 
		- **Explicit copy**: only a special operation can access a remote register under compiler control and must be inserted in a special place in the code. This may increase instruction issue pressure and code size.  
	- Implementation Constraints 
		- Implicit and explicit copy operations increase critical path 
		- Dividing a single architecture into two cluster costs 15 - 20% extra cycles, four clusters cost 25 - 30%. The reason for the increase is the explicit copies and increased requests on memory. If we have 15 - 20% increased clock speed and bypass logic, clustered configuration becomes the better choice. The increased clock frequency is modest, so this is a **viable choice** for VLIW.   
	- Full connectivity is not necessary between the clusters. Partial interconnectivity improves scalability. Partitioned files use less area and dissipate less power. The bypass network is partitioned and hierarchical.    
		- Partitioning By Data Types 
			- Partitioning is sometimes done by data types: integer and floating point registers. 
			- Predicate register banks - the contents of the registers do not commit until the predicates come true. 
			- Branch register banks - which branch is to be executed 
			- These provide good reachability by simple copy method, otherwise compiler optimization may be too conservative. Turning the banks on and off determine the data flow.     

### Address and Data Registers 
- In VLIW **register files are general purpose**. The compiler allocates registers regardless of their intended use. 
- In DSP architectures there are address and data registers. 
	- Address registers access memory
	- Data registers used for data manipulation. The registers can be used for different data widths. Certain registers can only access certain functions. This can lead to redundant register movements. This can lead to compilation complexity.

### Register File Addressing
##### Index Register Files
how to go to a specific register in a file?
- base + offset
- there is a small compiler-managed cache of the machine stack
- Frame: the area where the inputs, outputs, and variables of a function call reside. The compiler can explicitly allocate a variable sized section of the register file by processing the frame. The frame is used for procedure call and return for  stack management. The advantage of allocating the frame in a register file is it eliminates register spills and restores at call boundaries. 
	- register spill → when a function is called, all the variables in the register file must be stored in memory before the new variables can be loaded into the file.
	- restore → when the function is called again, the variables have to be called from memory and restored to the register file. 
	- Register spills and restores result in a very high overhead at the boundaries.
	- ![[index reg file.png|600]]

##### Rotating Register File
- Indexed register files for which the **base** of the file periodically cycles across a set of registers. As registers are needed, they are assigned in order. At the same time registers are being freed from the beginning of the list. As a result free registers are in the lower register addresses and occupied registers are upper register addresses. The illusion is the base shifts up the addresses. Rotation is a form of dynamic register renaming. This is useful for software pipelining. The compiler can generate small, compact codes using rotating register files. 

##### Cost
Both indexed and rotating files have implementation costs:
- Indexed: adding offset and base values is a small delay but it sits in the critical path and may slow down the register file. 

### Addressing Mode
Addressing computation are done in **Execution stage** of instruction pipeline. When the addressing modes are simple, the latency shrinks, but the number of instructions increases. And reduces the flexibility of the compiler to rearrange data.

Most accesses are map using base + offset. Structures and arrays use this method, the compiler calculates the offset. Using this mode is important in VLIW because code size is important. Without this mode two operations are needed, which increases code size. Many times the offset can be a constant and does not need to be calculated. In many embedded systems, there is a dedicated adder for address calculation. This is called the **address generation unit, and is done at post-increment**.

### Addressing Sizes
data path width can be 8 or 12 bits. And 5 bits path can be used to store temporary values in **RAM registers**
![[address size.png|600]]

Wider accesses: **register-pair**. Two consecutive registers, upper and lower portions of the operand. 
- These will require special instructions. 
- It is also possible to have subword access in each register in the pair without additional codes to even expand parallelism. 
- A dedicated multiplex used to overlap two consecutive accesses of register pair. 
- example register pair: _double in C_.

##### Exotic Addressing
![[exotic addressing.png|600]]
- Note
	- Uncached memory accesses or on-chip accesses: the data comes directly from the memory, bypassing the cache. Sometimes special addressing modes are used (LD.M = fetch data from main memory). 
	- Harvard architecture tricks: use inst bus line as additional data line to increase the bandwidth. 
	- XY Memory Addressing Mode: used in convolutional codes. Stream two large arrays to reduce latency. 
	- Circular Addressing Modes: accessing addresses in a very large pattern. The data is stored in memory so that it can be addressed by simply shifting the address in the register with a left shift. Common in signal processing. 
	- Bit Reversed Addressing: in Fast fourier transforms (FFT) bits are flipped. Given the address of a particular element in the array, the dsPIC hardware automatically computes the address of the next element in the [bit-reversed sequence](http://microchip.wikidot.com/dsp0201:bit-reversed-addressing).

##### Alignment Issues
When loading register pair, it can be tricky because the data can be misaligned in memory. This can be corrected by shifting bits when the two registers are combined into one atomic chunk for CPU.

Misaligned access can cause an exception:
- VLIW will treat misaligned registers accesses simply as **non-recoverable exception**, discarding the whole registers.

# Memory Architecture
**VLIW is a load/store architecture that mostly reuses RISC memory-addressing concepts**. The loads are separate and must be done before any operations can be done on them. VLIW support special addressing modes. 

**Registers hold data and address **
- so compilers have more flexibility and control.
- memory is banked and therefore power efficient
	- memory banks → a block of memory is separated into different sections. This will lead to concurrent access to memory. This is called X-Y memory, the x bank provides the first operand, the second bank provides the second operand
- **GPUs** are special embedded systems. 
	- They have constant memory - all constant variables are stored in a memory block
	- shader memory - a group of variables that are used together are stored together. For example: the information on a pixel. Shader memory efficiently supports group access
	- shared memory - used for memory that is shared between different threads.
	- local memory - memory that is just for a specific thread. Separating operands into specific memory increases bandwidth. Users can assign operands to specific memories -- lately compilers have taken over some of this responsibility

##### Cache Prefetching
Anticipate and prefetch blocks from memory into cache ahead of time, may waste bandwidth and result in cache pollution if guess is wrong.
- Replacement policies try to void replace cache blocks that has spatial locality or temporal locality
- Stream buffers: 
	- A special kind of cache. It acts like a data cache for only spatial locality. This is FIFO. (first in first out)

##### VLIW deterministic memory latency for real-time
For embedded systems latencies should be small and non-variable. Latencies should be the same each time the program is executed because of the interaction with users. If the latency is variable, users may conclude there is a problem with the hardware. Most caches have variable latencies, so embedded systems use **local memories** and **lockable caches**. 
- A local memory is a memory whose data are controlled by compiler or programs. 
- A lockable cache means some of the data is not evicted.

The benefits of these techniques:
- deterministic memory latencies control for real-time
- need not obey inclusion properties (making it space efficient) → the cache behaves more like a scratch pad, not all data needs to be stored in memory or duplicated in  multilevel caches.
- Compiler controlled scratchpad memory
- Content addressable memory → access to the memory can be very fast using this method, also known as associative memory. “It compares input search data (tag) against a table of stored data, and returns the address of matching data“