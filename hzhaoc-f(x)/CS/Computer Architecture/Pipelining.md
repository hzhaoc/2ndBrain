Pipeline is a sequence of multiple stages to process instructions from start to end. A typical basic five-stage pipeline in a processor is:
`Fetch -> Read/Decode -> ALU -> Memory Access -> Write the Registers`

## Pipeline CPI:
Ideally, after pipeline is filled with instructions, CPI (cycles per inst) will be one since one inst is completed per stage. (**I assume one stage is one cycle**).

Assume ideal CPI = 1:
- Pipeline fill
Pipeline filling makes $CPI\geq1$.

- **Pipeline stall**
If there an instruction has to wait at a pipeline stage, all the instructions ahead of it proceed through the pipeline, all the instructions behind it are also stalled. This is called a delay in the pipeline. The pipeline ahead of the delay will not have instructions to execute as the pipeline empties and the instructions behind the delay will be stalled. Pipeline stall makes $CPI\geq1$.
![[pipeline-jump.png]]

- **Pipeline flushes**
Branches can cause bubbles when the incorrect branch is taken. When this happens all the incorrect instructions that were fetched must be flushed from the pipeline and replaced with NOPs. Then the correct instructions must be fetched.
![[pipeline-jump.png]]

## Dependencies
Dependencies are due to program, not pipeline.
### control dependencies
- Inst: **Branch/Jump**
About 20% of insts are Branch/Jump.
- Inst: **Taken insts** (actually go to jump inst) are 50% of Branch/Jump insts.

### data dependencies
- **True** (some can be **hazards**)
	- RAW (read after write / flow)
- **False**
	- WAW (write after write / write over)
	- WAR (write after read / anti)

### dependencies and hazards
For program control dependencies hazards, FLUSH.
For data dependencies hazards, INSTALL or FOWARD.

### overall CPI
Overall CPI = CPI of program + % of insts mispredicted * penalty for misprediction.

## How many stages
When stages are increased in a pipeline, clock rates increase, at the same time CPI will be higher due to more hazards from deep stages, overall leading to, according to [[Computer Architecture|Performance]] formula, higher CPU active power, and, according to [[Computer Architecture|CPU time]]/execution time formula, CPU time decreased or increased where there will be an optimal performance for some number of stages. If 30~40-stage pipeline has optimal performance only, usually 10 - 15 stages are better when CPU power consumption is also considered.