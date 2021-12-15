# VLIW compiler
> So what is VLIW? Although VLIW is often referred to as an "architecture," it is most accurate to say that VLIW is an **architectural design philosophy or a design style**. A design philosophy is, in essence, an informal set of guidelines, principles, and common building blocks that distinguish one processor design from another. There is no easy litmus test that tells you whether a given processor was built following a given design philosophy, since this is rarely a black and white issue. However, people experienced in the field of computer architecture will agree on whether it was, and to what extent.

### reasons VLIW compiler can be used in embedded systems
- less hardware cost/complexity
- thus more energy efficient
- also no need to be general purpose (machine specific opt)
- thus easy to scale (compiler does work instead of hardware) and customize
- embedded systems code is less complex, more predictable, thus ILP can be handled by compiler opt
- embedded systems code changes and being rebuilt often, thus code compatibility issue is not that of a big deal
- **cons**: also due to frequent system upgrade, VLIW compiler is not that backward compatible.

### layer
- **front end**
	- language dependent: e.g. Java, C++
- **middle end**
	- machine independent, high-level optimizer
- **end end**
	- IR-to-machine code, ILP oriented optimizations

### opt
- code reordering to capture parallelism by **global** inst scheduler and code layout opt
- interact with **machine-specific** opt
	- e.g. reg allocation is open research topic

### glob vs local inst scheduler
![[glob vs local inst scheduler.png|600]]

### role of VLIW compiler
- bundle, schedule independent operations into long instructions
- resolves structural and resource hazards according to hardware constraints
- if the VLIW is clustered, **the compiler assigns operations to clusters and generates cross cluster register references**

### subtle problems to tackle in VLIW
- horizontal: decisions within the instruction word
- vertical: decisions across pipelined instructions
	- The compiler uses the maximum latency. What happens if the operation completes before its maximum latency?
		- **EQ (equal) Model**: stall until assigned latency expires, but this will lead to difficulties with exceptions, and it is inefficient
		- **LEQ Model**: (less-than-or-equal model): an operation may complete in fewer cycles. This is an efficient model. It is better at handling exceptions because it can use the extra time to handle exceptions.