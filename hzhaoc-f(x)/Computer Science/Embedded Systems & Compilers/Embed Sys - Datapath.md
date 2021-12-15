![[VLIW data path.png|600]]

**The Data path:**
- The controller makes sure the data is latched into the buffer properly, coordinates ALU operations, and checks for hazards. In VLIW datapath is the collection of its execution units, which performs data transformation

**CISC and DSP:**
- all the operands reside in memory. So there must be memory-to-memory operations and complex addressing modes. There are accumulators: which are target registers of the ALU. This means the compiler is forced to make binding choices and optimizations too early to reduce the memory traffic.

**VLIW and RISC**
the operands are in the registers before any work is done that uses them. This means there needs to be a lot of registers, especially since all there are multiple instructions executing in parallel. All those instructions need data stored in registers. The compiler must be very aggressive with register allocation. **The compiler must decouple scheduling and register allocation**. So first scheduling is performed, then the register allocation is done.

**Datapath Operations Cycles**
- The 32 bit processors take way more cycles than the 16 bit versions because the 32 bit operations break down the operations into 16 bit operations and use the carry bit to extend the size. 16 bit buses operate much more efficiently than 32 bit buses.

**Datapath Width**
> The data path width refers to the number of bits that are transferred within the computer, for example between the CPU and the memory. The more bits are transferred simultaneously, the faster the computer works.

- The width of the datapath equals the width of the registers that hold int and float. Sometimes two different widths of the datapath are supported. If only integers are supported, the time for floating point operations will greatly increase. The initial versions for ARM did not support floating point operations, it was done through a software library. This made the processors extremely efficient, but the time for floating point operations was 100s of clock cycles. CISC and RISC usually have two data paths, each the width of the datapath. Often the integer datapath is narrower than the floating point one. In DSPs datapaths are likely to be 40 bits or 56 bits, this are ADC widths.

**VLIW Datapath Widths**
- There are 8 - 32 bit independent datapaths.
![[VLIW datapath width int.png|600]]
- The same datapaths can be reconfigured to support floating point operations. 
![[VLIW datapath width float.png|600]]

##### ISA Minimum Requirements
- Minimum commands for accessing memory: 
	- load
	- store
- Minimum commands to perform arithmetic functions: 
	- subtraction
- Minimum commands for control functions
	- less than zero, 
	- equals zero, 
	- branch unconditional

## Operation Repertoire
##### Integer Multiplication
Multipliers are large and slow. In VEX the multiplication is broken down into smaller operations. The 32 bit multiplication is divided into two 16 bit multiplications: upper and lower. There is a NOP inserted to allow for the delay created with the multiplication. After multiplying the upper and lower sections, the products are added together to get the answer. This way, we save data path width to only 16bits and improves latency efficiency.

##### Fixed-Point multiplication
- 2 low precision operands multiplication. The right shift is used to get the MSB (most significant bits) in place. This results in starting with 16 bits and ending with 16 bits.
- higher precision multiplication like 32 bits can also be supported but expensive (2021)
- often seen in DSPs and rDBMS
![[VLIW fixed point mult.png|600]]

##### Integer Division
- Division is more expensive than multiplication. It’s more complex because the answer may be an integer or a floating-point value. When no FPU (float point unit) is available, in div is rarely supported. 
	- In VEX, divs instruction is provided for basic component for an integer division. 
	- Non-restoring 32-bit division can take 35 cycles
	- The compiler may optimize shorter divisions or divisions by constants.
	- Division is rarely critical and many systems favor code size to hardware design.

##### Saturated Arithmetic 
Occurs when you try to exceed the precision that is allowed for the implementation. In standard C semantics imply a wrap around. For example: a 32 bit int 0XFFFFFFFF. If we add 1 to it, the result is 0X00000000, resulting in an overflow. Normally this is fine. But in embedded domains overflows are not acceptable, so saturated arithmetic (get a value at cap) is used.   
![[saturated arithmetic.png|600]]

## Parallel micro architecture
##### VLIW vs SIMD
In VLIW instruction sets, each instruction works on only one data set. There can be multiple instructions and multiple data sets.   
![[parallel function unit arch.png|600]] 

##### SIMD
In SIMD instruction sets, the same instruction works on a large quantity of data.  
![[simd arch.png|600]] 

##### microSIMD
microSIMD Parallel Subword Architecture: 64 bit FU can process words as 1 64 bit, 2 32 bit, or 4 16 bit. This means data can be compacted and be fit into a long 64 bit word. Speeds up processing and reduces data size requirements. Very popular: x86    
![[microSIMD arch.png|600]]

- microSIMD parallel operation e.g.
PADD4 - breaks down larger words into sub words. Then adds 4 sub words together. Then operate on the four sub words.    
![[microSIMD ops eg1.png|600]] 

- microSIMD predicate control flow e.g.
![[microSIMD ops eg2 predicate.png|600]]

- microSIMD another parallel ops (reductions) e.g. 
	- Note that psum is stored to different registers by renaming in each iteration and summed up only at the end.
	- ![[microSIMD ops eg3 reduction.png|600]]

**Practical Difficulties**
- Alignment issues 
	- are a problem when breaking into subwords. Structures that contain subword elements rarely align cleanly to word boundaries. 
	- to align data, unoptimized pre/post loop codes are needed.
- Precision Issues 
	- there may need to be a few extra bits for holding intermediate stages of an algorithm.  

**Micro-SIMD pros and cons**
- Can achieve impressive results with a minimal hardware complexity
- complete set of micro-SIM extensions costs too much. For example it is not usually done for division
- automatic extrications micro-SIMD w/o hints by the compiler is still unproven.
- Manual code restructuring is still needed to exploit micro SIMD-parallelism     

**Summary**
- microSIMD can do only specific specifications, VLIW is for much more general purpose parallelism
- The number of register files is much less for microSIMD. There is a cost, the width of the microSIMD is 64 bits - very wide! VLIW can do four different kinds of instructions, while SIMD cannot. VLIW is better for more general parallelism.  
![[parallel arch summary.png|600]] 

## Constants
- Specifically the immediate operands and literals. Some constants are known at compile time, others at load time. 
- Short immediate constants tend to be used in **addressing modes** and fit in a single encoded operation. Long immediate constants can be the width of the datapath. There are two methods for long immediates:
	- partial immediate load 
	- memory allocated immediate - in this case the compiler allocates long immediate in memory and emits an instruction that loads the immediate. 
- Branch offsets are also immediate. The largest branch offset size means the area of code that is reachable from the branch. There can be a maximum jump size. ­ 
	- MIPS - the jump instruction has 26 bit wide offsets.
	- PC is word aligned in MIPS, so you can jump 28 bits.
	- PC relative addressing and many addressing modes 
	- 32 embedded ISA includes a branch offset large enough to cover local branches If you need a larger jump, you will have to chain the jumps.  In 64 bit address space you will need to chain jumps also if necessary. So as a result you do not need large branch jumps in the ISA