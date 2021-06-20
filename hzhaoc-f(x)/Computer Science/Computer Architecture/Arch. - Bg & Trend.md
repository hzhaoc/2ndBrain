##  Intro
Assembly language programming elimination and standardized vendor-independent operating systems creation such as UNIX bring out a new set of architecture with simpler instructions called RISC (Reduced Instruction Set Computer). RISC-based machines focused on two performance techniques: 
- instruction level parallelism ([[ILP - ILP & Deps.]], initially pipelining)
- cache optimization

RISC-based computers outcompeted peers. Intel rose to challenge primarily by translating 80x86 instructions into RISC-like instructions internally. As transistor counts soared in 1990s, hardware overhead of translating the more complex x86 architecture became negligible. In low-end applications such as cell phones, this overhead led to a RISC architecture,  **ARM**, becoming dominant.

In 1974,  Robert Dennard observed **Dennard scaling**: power density was constant for a given area of silicon even with increased number of transistor because of smaller dimensions of each. Transistors could go faster but use less power. Dennard scaling ended around 2004 because current and voltage couldn't keep dropping and still maintain dependability of integrated circuits. This change **forced** processor industry to use multiple efficient processors or cores instead of uniprocessor. This switch is not optional at the time. It indicates architect focus transitioning from solely relying on ILP to data-level parallelism (DLP), thread-level parallelism (TLP), request-level parallelism (RLP) among WSCs (warehouse-scale computers). Whereas compiler and hardware conspire to exploit ILP implicitly without programmer's attention, DLP,  TLP, RLP are explicitly parallel, requiring restructuring of applications for such types of parallelism, a new burden for programmers.

Second observation is **Moore's Law** which is number of transistors per chip would double every two years. It ended somewhere around 2010.

The ending of Moore's Law, Dennard Scaling, unchanging power budgets for microprocessors, replacement of power-hungry uniprocessor with energy-efficient multiprocessors, limits to multiprocessing to achieve **Amdahl's Law**,  together cause improvement in processor performance to slow down. And the only path left to improve **energy-performance-cost** is **specialization** - **domain-specific cores or processors.**

## Classes of Computers
- Internet of Things (IoT) / Embedded computer
- Personal mobile device
- Desktop/Laptop Computing
- Server
	- Availability
	- Scalability
	- throughput
- Clusters / WSCs
	- A collection of **desktop computers or servers** connected by local area networks to act as a single larger computer. Each node running its own operating system, and nodes communicate using a networking protocol.
	- Focus on performance and power.
	- Difference between WSC and server is WSCs use redundant inexpensive components as building blocks, relying on software layer to catch and isolate many failures in computing to deliver availability needed for such applications. Scalability is handled by networking protocol instead of integrated computer hardware as in the case of servers. 

## Classes of Parallelism
### Application level
- ##### DLP
data-level parallelism arises because there are many data items that can be operated at the same time.
- ##### TLP
Task level parallelism arises because tasks of work are created that can operate independently and largely in parallel.
### Hardware level
to implement application level parallelism, hardware can in turn exploit in four ways:
- ##### ILP
_instruction-level parallelism_ exploits _data-level parallelism_ at modest levels with compiler help using ideas like **pipelining** and at medium levels using ideas like **speculative execution**.
- ##### Vector architecture, GPUs, multiple instruction sets
applying a single instruction to a collection of data in parallel.
- ##### TLP
thread-level parallelism exploits either data-level or task-level parallelism in a tightly coupled hardware model that allows for interaction between parallel threads.
- ##### RLP
request-level parallelism exploits parallelism among largely decoupled tasks specified by the programmer or the operating system.

## Define Computer Architecture
- ##### [[Inst Set Arch.#Instruction Set Architecture|ISA]]: myopic view of computer architecture
- ##### Genuine computer architecture
software function needs demand computer architecture

## Trends in Technology
- *Integrated circuit logic technology* — Moore's Law ended.
- *Semiconductor DRAM* — seemingly no 32-GB DRAM.
- *Semiconductor Flash* — electronically erasable programmable read-only memory. Standard storage device in PMDs. SSD is rapidly increasing and replacing magnetic disk. A lot cheaper than DRAM.
- *Magnetic disk technology* — a lot cheaper than flash memory. Central to server and WSCs.

##### Scaling of transistor and wires
To a first approximation, in the past, the transistor size decrease linearly or **count increase quadratically** with **linearly increase in overall performance**. And wires do not. **Wire delay** is a design obstacle for large integrated circuits. **Larger and larger fractions of clock cycle have been consumed by propagation delay of signals on wires, but power now plays an even greater role than wire delay**. 

## Trends in [[Arch. - Power & Energy]] in Integrated Circuit


## Trends in [[Arch. - Cost]]


## [[Arch. - Performance|Performance& Reporting]]


## Quantitative Principles of Computer Design
- parallelism
- locality
- common use priority
- [[Arch. - Performance|Amdahl's Law]]

## Fallacies & Pitfalls
- all exponential laws must come to an end
- multiprocessors trend is because there's no other option
- redundant system components to avoid single point of failure (fault-tolerant)
- benchmarks don't remain valid indefinitely
- disks never fail
