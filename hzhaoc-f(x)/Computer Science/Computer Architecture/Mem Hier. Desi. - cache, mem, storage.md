# Overview
![[mem_hierarchy.png]]

- The gap between CPU memory demand (# requests / second) & DRAM bandwidth was growing. This effect is called **memory wall**. Recently the gap growth slowed down due to limited performance growth of a single processor. However, the gap between high-end multiprocessors memory demand  & DRAM bandwidth continues to grow. 
- Traditionally, designers focused on optimizing **average memory access time (AMAT)**, determined by **cache access time**, **miss rate**,  **miss  penalty**; More recently, **Power** is a major consideration. In some PMD cases, caches can account for 25% to 50% of the total power consumption.

# Cache
> Check [[Cache Basic]] note for detail introduction

In cache, data move by **block** (multiple words). Each block includes a **tag** to indicate which memory address it corresponds to. A key design decision is where blocks can be placed in a cache. The most popular scheme is *set associative*, where a set is a group of blocks in the cache. A block is first mapped onto a set, and then the block can be placed anywhere within that set. Finding a block consists of first mapping the block address to the set, and then searching the set to find the block. The set is chosen by the address of the data:
$$(block \ address)\ MOD \ (Number \ of \ sets \ in \ cache)$$

If there are *n* blocks, it is called *n-way set associative*. A *direct-mapped*  cache has just one block per set. A *fully-associative* cache has just one set.

Caching writes is a bit difficult. A  *write-through* cache updates item in cache and writes through to update the main memory. A *write-back* cache only updates copy in the cache, and when the block is to be replaced, it is copied back to memory. **Both methods require a *write buffer* to allow the cache to proceed as soon as the data are placed the buffer rather than wait for full latency to write the data into memory.**

##### Cache Miss Category
- *compulsory*
- *Capacity*
- *Conflict*
- *Coherency*
Detail see  [[Cache Basic#Cache Miss Category]]

##### Cache Performance Measurement
Average memory access time (AMAT) = Hit time + Miss Rate X Miss penalty

##### Cache Optimization Techniques
Detail see [[Cache Optimization]]

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

# Memory Technology
access time: time between when a read is requested and when the desired word arrives;
cycle time: minimum time between unrelated requests to memory.

![[real mem chip.jpg|800]]

### SRAM Technology
![[SRAM_Cell.png|300]]
Static-random-access-memory. SRAM doesn't need to refresh/ write back data after being read, unlike DRAM. Thus access time is very close to cycle time.

On-chip caches use SRAMs. Organized with a width that matches block size of the cache. This allows an entire block to be read or written within a single cycle. The access time to the cache is proportional to the number of blocks in  the cache, whereas the energy consumption depends both on the number of bits in the cache (static power) and on the number of blocks (dynamic power). 

### DRAM Technology

![[DRAM_Cell.png|300]]

To prevent loss of information as the charge in a cell leaks away, each bit must be "refreshed" periodically. All bits in a row can be refreshed by reading that row and  writing it back. Every DRAM in the memory system must access every row within a certain time window, such as 64ms. DRAM controllers include hardware to refresh DRAMs periodically. Designer try to keep time spent refreshing to less than 5% of the total time.

###### SRAM vs DRAM
- SRAM is faster than DRAM, but requires more transistors per bit.
- Both requires power on to sustain data
- memory chip organization
	- refresh per row
	- fast page mode: open a mem row -> row buffer get bits -> read & write with that buffer -> close the page. this way, read & write to same row can happen at the same time.
	- connect to processor
		- DRAM is accessed to the processor through the front-side bus using a memory controller. The downside of this is the DRAM must be much more standardized and inflexible to work with the on-chip memory controller
	- ![[mem_row_col.png]]

##### Inside a DRAM: SDRAM
Synchronous DRAM. 
- Designers added a **clock signal** to the DRAM interface so that repeated transfers would not bear the overhead to synchronize with the controller. 
- SDRAMs also allowed addition of a **burst transfer mode** where multiple transfers can occur without specifying a new column address.
- A new innovation in early 2000s: **double-data-rate** (DDR) which allows a DRAM to transfer data both on the rising and the falling edge of the memory clock, thereby doubling the peak data rate.
- SDRAMs introduced **banks** to help with power management, improve access time, and allow interleaved and overlapped accesses to different banks.
DRAMs are commonly soled on small boards called *dual inline memory modules* (DIMMs) that contain 4-16 DRAM chips and that are normally organized to be 8-byte wide for desktop and server systems.
##### Graphics Data RAMs
GDRAMs or GSDRAMs are a special class of DRAMs tailored for handling higher bandwidth of graphic process units. 
Differences from normal CPU DRAMs:
1. wider interface. 
2. higher maximum clock rate on the data pins. GDRAMs normally connect directly to GPU and attached by soldering them to the board, unlike DRAMs, which are normally arranged in an expandable array of DIMMs.
##### HBM
Newest innovation in 2017 in DRAMs is packaging. It places multiple DRAMs in a stacked or adjacent fashion embedded within the same package as the processor. Processor & RAM in same package enables lower latency & higher bandwidth. It is also called **high bandwidth memory (HBM)**.
![[DRAM stacking.jpg]]
One version is to place the DRAM die directly on the CPU die, using solder bump technology to connect them. Another way stacks only DRAMs and abuts them with the CPU in a single package using a substrate (interposer) containing the connections.
In some applications, it may be possible to internally package enough DRAM to satisfy the needs of the application.

### [[Storage Hierarchy#Flash Memory|Flash Memory]] Technology
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

# Storage
- files - program, data, settings.
- virtual memory

### magnetic disk
![[Secondary Storage Devices1.png]]
![[Secondary Storage Devices2.png]]
- access time
	- Seek time - time to move head assembly to the correct cylinder
	- Rotational latency - time to move to disk to the correct sector
	- Data Read - time required to read the entire sector 
	- Controller time - time to check data (check sum, etc)
	- I/O Bus time - time to load data on the bus and send to processor
	- Only one disk access can be performed at a time, so there is an additional: Queuing delay - time to wait for availability of the disk
- Trends for Magnetic Disks
	- Capacity is improving
	- Seek Time has slowly improved
	- Rotation Speed has improved
	- Controller and Bus Speed have improved
- [[Mem Hier. Desi. - storage fault tolerance]]
### optical disk
Optical disks (such as CDs and DVDs) are similar to magnetic disks.Since they are portable, they need to be standardized, which slows improvement.

### magnetic tape
large capacity, low production and demand, sequential access, 2nd storage, cheaper than magnetic disk.

### solid-state disk
- DRAM + Battery: fast, expensive, lose content when out of power
- Flash: fast, keep  data without power, smaller capacity than magnetic disk

### hybrid magnetic flash
flash as cache for hard disk.

# Connecting IO Devices
IO devices are connected to the system with a bus.The buses must be standardized to connect to a number of IO devices, so improvement to the bus are slow.