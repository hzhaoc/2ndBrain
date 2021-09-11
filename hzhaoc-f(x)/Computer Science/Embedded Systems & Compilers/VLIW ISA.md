### Overview
ISA allows the designer to treat the processor as a black box. Understanding the ISA can help determine which processor to use for a given system.

ISA serves as a layer between software and hardware. So what to expose to and what to hide from software?
- Inst Sche: VILW exposes it to software (compiler); superscalar hides it
- pipelining: (Implementation is hidden or exposed as a design choice)
	- Completely hidden pipelining example: [[ILP - OOO EXE|Out Of Order Execution (Tomasulo's)]], the hardware does all the work
	- Exposed example: Early RISC machines had exposed delay slots
	- VLIW: the pipeline is exposed at either architectural or implementation level

### Instruction Encoding
![[encoding comparison.png|600]]
- **variable** here means static variable operations in one instruction
- **dynamic** here means variable operations determined in run time
##### how to reduce size for VLIW encoded instruction?
- remove two types of NOPS
	- vertical NOPS due to exposed latencies
		- multicycle NOP directive
	- horizontal NOPS by limited parallelism
		- start-bits or stop-bits

##### fixed-overhead encoding
- used in first gen VLIW
- prepending mask bits to tell how to map to a expanded full inst buffer
- also compute next PC 
- advantages:
	- simple
	- space overhead for mask

![[mask inst encoding.png|600]]

##### distributed encoding
- variable-overhead encoding
	- the more NOPs, the more stop bits
- no need to compute next PC
- requires more complex decoding logic

##### template-based encoding
- there certain predefined schemes/templates that does specific mapping to full VLIW buffer
- may run out of templates

![[template-based inst encoding.png|600]]

##### ISA extensions
new insts get to added to ISA all the time. this may create problem for encoding. but VLIW rarely adds new extensions.