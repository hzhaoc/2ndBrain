# Overview 
There are four major storage levels.
1. Internal – Processor registers and cache.
2. Main – the system RAM and controller cards
3. On-line mass storage – Secondary storage
4. Off-line bulk storage – Tertiary and Off-line storage.

# Hierarchy
## Register
A **processor register** is a quickly accessible location available to a computer's [[CPU|processor]]. Registers usually consist of a small amount of fast **storage**, although some registers have specific hardware functions, and may be read-only or write-only. In [[Computer Architecture]], registers are typically addressed by mechanisms other than *main memory, but may in some cases be assigned a *memory address* e.g. DEC PDP-10, ICT 1900.

Almost all computers, whether *load/store architecture* or not, load data from a larger memory into registers where it is used for *arithmetic operations*, and is manipulated or tested by *machine instructions*. Manipulated data is then often stored back to main memory, either by the same instruction or by a subsequent one. Modern processors use either [static](https://en.wikipedia.org/wiki/Static_random-access_memory "Processor (computing)") or [dynamic](https://en.wikipedia.org/wiki/Dynamic_random-access_memory "Dynamic random-access memory") [RAM](https://en.wikipedia.org/wiki/Random-access_memory) as main memory, with the latter usually accessed via one or more [cache levels](https://en.wikipedia.org/wiki/CPU_cache#Multi-level_caches "Random-access memory").

Processor registers are normally at the top of the *memory hierarchy* (see above) , and provide the fastest way to access data. The term normally refers only to the group of registers that are directly encoded as part of an instruction, as defined by the *instruction set*. However, modern high-performance CPUs often have duplicates of these "architectural registers" in order to improve performance via [[ILP - ILP & Deps.#Register renaming|register renaming]], allowing parallel and [speculative execution](https://en.wikipedia.org/wiki/Speculative_execution "Speculative execution"). Modern [x86](https://en.wikipedia.org/wiki/X86 "X86") design acquired these techniques around 1995 with the releases of [Pentium Pro](https://en.wikipedia.org/wiki/Pentium_Pro "Pentium Pro"), [Cyrix 6x86](https://en.wikipedia.org/wiki/Cyrix_6x86 "Cyrix 6x86"), [Nx586](https://en.wikipedia.org/wiki/Nx586 "Nx586"), and [AMD K5](https://en.wikipedia.org/wiki/AMD_K5 "AMD K5").

When a [computer program](https://en.wikipedia.org/wiki/Computer_program "Computer program") accesses the same data repeatedly, this is called [locality of reference](https://en.wikipedia.org/wiki/Locality_of_reference "Locality of reference"). Holding frequently used values in registers can be critical to a program's performance. [Register allocation](https://en.wikipedia.org/wiki/Register_allocation "Register allocation") is performed either by a [[Computer Science/Programming/Compiler|Compiler]] in the [code generation](https://en.wikipedia.org/wiki/Code_generation_(compiler) "Code generation (compiler)") phase, or manually by an [assembly language](https://en.wikipedia.org/wiki/Assembly_language) programmer.

Registers are small memories within the cpu. They are nearest to the cpu. There are many types of registers like Accumulator, Data Register, Program Counter, General purpose, etc. Thus they can be used for various tasks.

Take example of accumulator register, its aim is to hold partial results and calculations. For example, if you want to multiply 789653 with 23442 i.e. (789653\*23442), then you must store intermediate results and calculations before the final summation. This is the specific task of accumulator register.

Take another example of Program Counter, it stores the address of the next instruction to be fetched.

## Cache
It's a temporary storage. It resides within the processor chip. It's both very fast as well as nearer to cpu than ram. The main aim is to try to fill it with the data which might be needed again soon. Hence it speeds up the computations if next time cpu finds the required data in cache itself (& thus no need to search & fetch data from slower ram).

There are various techniques to efficiently use the limited cache memory like Least Recently Used (LRU), etc. These techniques tries to predict which data might be needed again & hence should be stored in cache.

It's of generally three types/levels, L1, L2 & L3. L1 is the fastest but smallest. L3 is the largest but slowest.

> Check [[Mem Hier. Desi. - cache, mem, storage#Cache]] for cache introduction under memory hierarchy.

## Memory
(Main) Memory is located external to the CPU. Generally speaking, data has to be loaded into a CPU register from memory before the CPU can process it, memory is much slower than registers and caches, and there is a lot more memory capacity than registers. Generally memory can be addressed on a byte boundaries, where registers may not be able to access all the bytes in a register (?).

##### RAM
check [[Mem Hier. Desi. - cache, mem, storage#Memory Technology]] for DRAM & SRAM introduction. 

RAM stands for Random Access Memory. Physically, it is a series of chips in your computer. When your computer is turned on, it loads data into RAM. Programs that are currently running, and open files, are stored in **RAM**; anything you are using is running in **RAM** somewhere. As soon as the electricity to the **RAM** is cut, it forgets everything; that's why an unsaved document is lost if the computer locks up or there is a power failure.

## Storage
#### Flash Memory
Because it uses integrated circuit technology, flash storage is a **solid-state technology** (SSD). SSDs got their name—solid state—because they have no moving parts. In an SSD, all data is stored in integrated circuits. This difference from HDDs has a lot of implications, especially in size and performance. Without the need for a spinning disk, SSDs can go down to the shape and size of a stick of gum (what’s known as the M.2 form factor) or even as small as a postage stamp. Their capacity—or how much data they can hold—varies, making them flexible for smaller devices, such as slim laptops, convertibles, or 2 in 1s. And SSDs dramatically reduce access time since users don’t have to wait for platter rotation to start up.

#### Hard Disk Drive
check [[Mem Hier. Desi. - cache, mem, storage#Storage]] for its various types. 

Main storage. As of 2021, PC main storage is SSD or HDD.  Large servers are usually HDD for main storage and backups. Typically, this type of storage is **magnetic**, and does not depend on **electricity** to remember what is written on it. However, it's much slower than **RAM**. Things on the hard drive need to be located, read and sent to **RAM** before they can be processed. If your computer says you are low on disk space you have too many programs or files on your computer. To correct this, you will need a new hard drive, or will need to uninstall unused programs or delete unneeded files off the computer.

###### SSD vs HDD
SSDs are more expensive than HDDs per amount of storage (in gigabytes, or GB, and terabytes, or TB), but the gap is closing as SSD prices begin to drop.

What makes SSDs an increasingly popular choice is their speed. Across the board, SSDs outpace HDDs because they use electrical circuitry and have no physical moving parts. This leads to shorter wait times when you’re starting up and fewer delays when opening apps or doing heavy computing tasks. A typical SSD from Intel with a middle-of-the-road 512 GB capacity ([Intel® SSD 760p Series](https://www.intel.com/content/www/us/en/products/memory-storage/solid-state-drives/consumer-ssds/7-series/ssd-760p-series/760p-series-512gb-m-2-80mm-3d2.html)) offers up to 10x faster read speeds and up to 20x faster write speeds than a midrange HDD (such as [Seagate 2 TB Barracuda\* 5400 RPM 128 MB Cache SATA\* 6.0 Gb/s 2.5" laptop internal hard drive ST2000LM015](https://www.seagate.com/www-content/product-content/barracuda-fam/barracuda-new/files/barracuda-2-5-ds1907-1-1609us.pdf)), which only offers data transfer speeds of up to 140 MB/s.