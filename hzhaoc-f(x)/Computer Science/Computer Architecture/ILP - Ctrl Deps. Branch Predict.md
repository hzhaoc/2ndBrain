# Basic
If a branch is not taken the PC (program counter) just advances to the next instruction; If the branch is taken the immediate value is added to the PC to advance to the new destination, it is not known until the end of the [[CPU|ALU]] stage whether the branch is taken or not. It is better to make a prediction for the instructions following branch instruction in the pipeline before branch instruction is taken, then the processor is at least right some of the time. 

A typical example program that has branch instruction:
![[inst_branch_eg.png|300]]

##### question to solve
- Is it a taken branch?
- What is the next PC? (where is the branch going? )

## Performance
> CPI = Ideal CPI + (Mispredictions / Inst) * (Penalty / Misprediction)

Mispredictions / Instructions is dependent on the predictor accuracy. Penalty / Misprediction is dependent on the size of the pipeline. The deeper the pipeline the more important it is to have an accurate branch predictor.

## Predictors
example pipeline

Fetch | Read/Decode | ALU | Memory Access | Write to Register
------ | --------------| -----| -----------------| ----------

### 1. none-predictor
**None-predictor** does not fetch instruction until it is know in `Decode` stage for non-branch inst, or it is decided taken or not in `ALU` stage.
-	Every branch costs 3 cycles. (Fetch, Decode)
-	Non-branches cost 2 cycles. (Fetch, Decode, ALU)

### 2. not-taken predictor
**Not-taken-predictor** predicts and just fetches next instruction:
- Every branch costs 1 or 3 cycles. (depends on the actual taken/not taken result in `ALU` stage).
- Every non-branch inst costs 1 cycle. (because it is not branch, it does not jump on PC, insts is just executed normally in the pipeline)
	
### 3. BTB PC predictor
Model: $$PC_{next}=f(PC_{now})$$
**BTB** (branch target buffer)
A table indexed by input PC, outputs predicted PC. Mapping steps:
1. At `Fetch` the processor has the PC of an inst.
2. Looks in the BTB for the PC.
3. Reads predicted PC in BTB.
4. Compares predicted PC with actual PC later  (`ALU` ?) in pipeline.
5. If not same, update BTB with new PC
- **Realistic BTB**
	- Limited number of PCs held in table according to insts coming to execution.
	- LSB (least significant bits) to index BTB.
	- Additionally, if insts are fixed-size 4-byte word-aligned, the lowest 2-bit are always `00`, so in BTB, we should take least significant bits starting the **3rd lowest bit** of PC.	![[Realistic BTB.png]]
	- For example, 32-bit/4-byte fixed-length register address, word-aligned (divided by 4),  what is an PC address `0x0000AB0C` mapped to in the least 10-bit significant BTB? Answer: in binary the address is `...1011,0000,1100`, lowest 2-bit is always `00` (aligned), the least 10-bit starts from 3rd lowest bit, result is `10,1100,0011`.

### 4. direction predictor
**Direction Predictor** uses a branch history table (**BHT**) to first determine if branch is taken or not **before BTB**. 
Model: $$PC_{next}=f(PC_{now},\;history[PC_{now}])$$
Steps:
1. Use LSB (least significant bits) of PC to index BHT.
2. BHT maps LSB bits to 1 bit that is `{0: not taken and PC++, 1: taken and go to BTB}`.
3. Similar to BTB, if mispredict, update to BHT. 

-	**1-bit predictor** 
![[BHT.png]]
The problem with 1-bit predictor is that when the not taken and taken branch insts are mixed in program. To solve this, there's a 2-bit predictor.

-	**2-bit predictor**
Enhanced/less-PC-pattern-sensitive direction predictor to predict branch taken or not.
	- `00`: strong not-taken
	- `01`: weak not-taken
	- `10`: weak taken
	- `11`: strong taken
	The predictor changes weak bit first when facing misprediction, reducing frequent updates that results in high misprediction rate in frequent taken/not taken switches. 
	
### 5. history-based direction predictor
**history based predictor** predicts branch taken or not based on last two actuals.
	
- 1-bit history with 2-bit counter
`1 bit history | 2 bit counter` This works well in not taken and taken branch insts interchange pattern: `(not taken, not taken, taken)*`
![[hist_based_predictor.png]]
	
- 2-bit history with 2-bit counter
Works well with $(NNT)^*$  (repeat (not taken, not taken, taken) ) pattern, or $(NT)^*$
	
- n-bit history predictor with 2-bit counter
It will predict all patterns of $length \leq n+1$. But cost **($n+2*2^n$)** bit per entry in the BHT. This can be needed in loops that's long $(N..NT)^*$ pattern.

### 6. history based with shared counter direction predictor
- #### PShare
Private history (each branch inst has its own history bits pattern in private history table / PHT). Shared counters (between all branches, in branch history table / BHT) - good for small loops and predictable short patterns. As shown in the picture below, instr PC and PC index mapped history together is the index for BHT, where the direction prediction is found and maybe updated
Bits cost much lower than n-bit predictor with 2-bit counters.
![[history_with_shared_counter_predictor.png]]
- #### GShare
Global history and shared counter - good for correlated branches.

### 7. Tournament predictor
Use a meta-predictor (2-bit counter table for instance) to select `{GShare, Pshare}` (More often GShare beats PShare). Use and Update both good predictors on each branch decision.
![[tournament_predictor.png]]

### 8. Hierarchical predictor
Similar to Tournament Predictor but usually better. Instead of using 2 good predictors, it uses 1 OK,  1 good. 
- Update OK predictor on each branch decision such as a simple **2-bit direction predict counter**
- Update **expensive** good predictor if OK predictor not good.

This way, you have a low-cost low-accuracy predictor & a high-cost high-accuracy predictor.

### 9. Return Address Stack (RAS)
Function return is a little different from other branch/jump inst in that the next/**predicted PC varies** (because function call can be anywhere in a program). 

Solution: Have a small separate stack RAS in hardware very close to CPU to store updated address of predicted inst PC for function `RET` inst PC. When an inst is calling a function, push its PC to RAS for return; when an inst is a function return,  pop  most recent pushed PC in RAS out and jump to that PC. In case there are nested functions,  RAS entries will be more than 1. When RAS is full, usually do **wrap around**, which means continue to fill newest PC and squeeze out oldest PC, (*rarely do **Not-Push** i guess*)

##### But how to know if it's a `RET` inst or not at  `FETCH` stage?
-	**Predictor**
Have a table store history PC which are `RET`.
- **Predecode**
When fetch inst from mem to cache, predecode it to add an additional bit for this inst to indicate `RET` or not `RET`. 

For example, CPU fetch instruction from cache; if not in cache, load inst from memory into cache, then fetched by CPU. When CPU load inst from memory into cache, PREDOCDE it by adding an additional bit to indicate whether this is a return instruction. Or you can design to let CPU Predecode it at fetching instruction from cache.

Predecoding is popular. It has other uses. For example, additional bit to indicate whether this  is a branch or not; for another, for variable length instruction set, additional bits to indicate length, so CPU can fetch next instruction more quickly and not rely on Decode stage.

## Avoid branch prediction
See [[ILP - Ctrl Deps. Branch Predicate]]