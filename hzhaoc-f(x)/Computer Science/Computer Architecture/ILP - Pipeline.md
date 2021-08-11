## Intro
Pipelining is the most common [[ILP - ILP & Deps.]] technique.
## Instruction Cycle
Pipeline is a sequence of multiple stages to process instructions from start to end. A typical basic five-stage pipeline in a processor is:

Fetch | Read/Decode | ALU | Memory Access | Write to Register
------ | --------------| -----| -----------------| ----------

### Fetch Stage
The fetch step is the same for each instruction:
1.  The [[CPU]] sends the contents of the [program counter (PC)](https://en.wikipedia.org/wiki/Program_counter "Program counter") to the [memory address register (MAR)](https://en.wikipedia.org/wiki/Memory_address_register "Memory address register") and sends a read command on the address bus
2.  In response to the read command (with address equal to PC), the memory returns the data stored at the memory location indicated by the PC on the data bus
3.  The CPU copies the data from the data bus into its [memory data register (MDR)](https://en.wikipedia.org/wiki/Memory_buffer_register "Memory buffer register")
4.  A fraction of a second later, the CPU copies the data from the MDR to the [current instruction register (CIR)](https://en.wikipedia.org/wiki/Instruction_register "Instruction register") for instruction decoding
5.  The PC is incremented so that it points to the next instruction. This step prepares the CPU for the next cycle.

The control unit fetches the instruction's address from the [[Storage Hierarchy|Memory Unit]]

### Decode Stage
The decoding process allows the CPU to determine what instruction is to be performed so that the CPU can tell how many operands it needs to fetch in order to perform the instruction. The opcode fetched from the memory is decoded for the next steps and moved to the appropriate registers. The decoding is done by the [[CPU]]'s [Control Unit](https://en.wikipedia.org/wiki/Control_Unit "Control Unit").
1. the control unit (CU) will decode the instruction in the CIR. 
2. The CU then sends signals to other components within the CPU, such as the [[CPU|ALU]] and the [floating point unit (FPU)](https://en.wikipedia.org/wiki/Floating-point_unit "Floating-point unit"). 
3. The ALU performs arithmetic operations such as addition and subtraction and also [multiplication via repeated addition](https://en.wikipedia.org/wiki/Multiplication_and_repeated_addition "Multiplication and repeated addition") and division via repeated subtraction. It also performs logic operations such as [AND](https://en.wikipedia.org/wiki/AND_gate "AND gate"), [OR](https://en.wikipedia.org/wiki/OR_gate "OR gate"), [NOT](https://en.wikipedia.org/wiki/Inverter_(logic_gate) "Inverter (logic gate)"), and [binary shifts](https://en.wikipedia.org/wiki/Bitwise_operation "Bitwise operation") as well.

### Execute Stage
The CPU sends the decoded instruction as a set of control signals to the corresponding computer components. If the instruction involves arithmetic or logic, the ALU is utilized. This is the only stage of the instruction cycle that is useful from the perspective of the end-user. Everything else is overhead required to make the execute step happen.

## Hazards handling (caused by program [[ILP - ILP & Deps.#Dependencies|dependencies]])
- **stall**
If there an instruction has to wait at a pipeline stage, all the instructions ahead of it proceed through the pipeline, all the instructions behind it are also stalled. This is called a delay in the pipeline. The pipeline ahead of the delay will not have instructions to execute as the pipeline empties and the instructions behind the delay will be stalled. Pipeline stall makes $CPI\geq1$.
Stall is for (actually only **true** because false ones are removed by reg renaming) **data dependencies**.
![[pipeline-jump.png]]

- **flush**
Branches can cause bubbles when the incorrect branch is taken. When this happens all the incorrect instructions that were fetched must be flushed from the pipeline and replaced with NOPs. Then the correct instructions must be fetched.
Flush is for **program dependencies**.
![[pipeline-jump.png]]

- **forward**
Forward is for example, at the first half of one cycle, the instruction return value is forwarded to input of following instruction for it to read correct value in the second half of the cycle, thus RAW is avoided. Forward is either forward from 1st half of cycle to 2nd half of cycle or forward from 1st cycle to next cycle.
Forward is for **data dependencies.**

- Summary
	- For program control dependencies hazards, FLUSH.
	- For data dependencies hazards, STALL or FOWARD. 

### overall CPI
Ideally, after pipeline is filled with instructions, CPI (cycles per inst) will be one since one inst is completed per stage. (**I assume one stage is one cycle**).

Assume ideal CPI = 1. Pipeline fill, stall, flush, increase CPI.

**Overall CPI = CPI of program + % of insts mispredicted * penalty for misprediction.**

## How many stages?
When stages are increased in a pipeline: 
- less work at each stage, so clock rates increase, at the same time CPI will be higher due to more hazards from deep stages, overall leading to, according to [[Arch. - Power & Energy|CPU dynamic power]] formula, higher CPU active power
- according to [[Arch. - Performance#Benchmark performance metrics|CPU time]]/execution time formula, CPU time decreased or increased where there will be an optimal performance for some number of stages. If only *performance* is considered, 30~40-stage pipeline is usually optimal; if *performance* and *power & energy* are considered, usually 10 - 15 stages are optimal.