- VLIW (very long instruction word) **offloads complete out-of-order instruction scheduling** & part of branching support from hardware to **compiler** for instruction level parallelism.
- VLIW processor do **one large instruction per cycle** that consists of multiple operations (regular instruction we saw is 1 ops/inst) where operands within one large instruction are found to be independent from each other. Thus compiler can sufficiently optimize inst scheduling without compiler support. And hardware cost & energy efficiency will be improved. 
![[VLIW vs superscalar.png|800]]

- Benefits
	- compiler does the OOO hard work. Compiler does this with plenty of time prior to program execution (hardware does it in run time with much less time room)
	- thus simpler hardware. less energy produced. less cost.
	- works on loops and "regular" code (code that does not do many decision makings in code)
- Downside
	- latencies can vary in run time (not deterministic in compiler time). for example, cache miss event.
	- no good on "irregular" applications such as machine learning
	- probly due to point 2, code bloat: lots of NOPS in one large inst because of many many interdependent operands.

##### VLIW Inst
- VLIW instructions have all the usual ISA opcode
- **Fully support compiler predication**
- Require many registers because of the scheduling optimizations
- **Branch hints because the compiler needs to tell the hardware its predictions**
- **VLIW instruction compaction**: instead of using NOPs for empty instruction slots there are stops. This reduces the number of instructions required, thus reducing code bloat.

##### VLIW examples
- ITANIUM
	- many ISA features 
	- very complicated hardware
	- still not great on irregular code
	- impossible to solve dynamic volatile cache miss latencies
	- failed and lost to AMD's x86-64
	- suggested reading [here](https://softwareengineering.stackexchange.com/a/279395)
	
> Load responses from a memory hierarchy which includes CPU caches and DRAM do not have a deterministic delay.

- [[Embedded Processor Market#categories by functions|DSP]] Processor
	- digital signal processing
	- regular loops, lots of iters
	- excellent performance
	- very energy-efficient