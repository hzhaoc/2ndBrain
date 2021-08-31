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