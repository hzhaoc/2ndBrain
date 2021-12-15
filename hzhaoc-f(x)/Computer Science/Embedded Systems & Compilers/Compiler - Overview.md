# Some Background
### [[Bg, Trend, Cost, Power, Energy, Perform#Intro|RISC]] vs CISC
![[RISC vs CISC.png|600]]
- RISC
	- lower per chip cost
	- require more instructions to do the same thing the CISC program does.
	- code expansion can be a problem
- CISC
	- reducing the gap between programming and hardware
	- makes more efficient use of a slow memory (many insts can access memory; in RISC there're only loads/stores)
	- instructions take different amounts of time to execute (variable length insts)

example of RISC vs CISC on same program:
- RISC:
```code
load r5 <- 4[r1]
add r5 <- r5 + r2
store 4[r1] <- r5
```
- CISC
```code
add 4[r1] <- r2
```

# Embedded System Market
## Categories by functions
as of **2010**
- **computational micros**
	- general purpose processors, such as CPUs of mainframes, PCs, workstations, servers, high-end portable devices. Most RISC or CISC based engines belong to this
- **embedded general purpose micros**
	- scaled-down versions of computational micros, such as ARM (Advanced RISC Machines), MIPS, x86
- **digital signal processor** (DSP)
	- focus on efficient execution of arithmetic operations in tight loop-oriented kernels. future will be VLIW-like designed (predictable and regular arithmetic code that has lots of ILP). market leaders: Texas Instruments, Motorola
- **microcontrollers**
	- industrial processors for standalone operations such as: memory, I/O, buses, peripherals in addition to a simple processing unit.
- **network processors**
	- similar to DSP in that it has incomplete connection networks and application-specific pipelines.
	- unlike DSP, it's usually programmed in assembly language, hard to compile. 
	- unlike DSP, it does not have high ILP, will not likely use VLIW structure in future

## Categories by market
as of **2010**
- imaging processing, consumer market
	- printers, audio, video, camera, home entertainment
- communication market
	- telephony, data networks
- automotive market
	- safety, engine control, navigation, brakes

## Language Processing System Overview
![[language-processing system overview.jpg|400]]

Some language processors combines **[[Computer Science/Programming/Compiler#Interpreter|Interpreter]]** and **[[Computer Science/Programming/Compiler|Compilers]]**. A high-level source program may be first converted to a intermediate program, like `__pyc__` for python, then a virtual-machine will compile the intermediary code immediately before run time.

### Structure of a [[Computer Science/Programming/Compiler|Compiler]]
- Analysis:
	- lexical analyzer/scanning
	- syntax analyzer
	- semantic analyzer
- Synthesis:
	- code generator (intermediate code -> machine code)

### Phases of a [[Computer Science/Programming/Compiler|Compiler]]
- lexical analyzer
- syntax analyzer
- semantic analyzer
- intermediate code generator
- machine-code generator

![[compiler structure.jpg|400]], ![[compiler structure 2.jpg|400]]