# Branch in a pipeline
If a branch is not taken the PC (program counter) just advances to the next instruction; If the branch is taken the immediate value is added to the PC to advance to the new destination, it is not known until the end of the [[CPU|ALU]] stage whether the branch is taken or not. It is better to make a prediction for the instructions following branch instruction in the pipeline before branch instruction is taken, then the processor is at least right some of the time. 

## Branch prediction question
- Is it a taken branch?
- What is the next PC? (where is the branch going? )

## Prediction accuracy
`CPI = 1 + (Mispredicted branch # / Inst #) * (penalty / mispred branch #)`
Mispredictions / Instructions is dependent on the predictor accuracy. Penalty / Misprediction is dependent on the size of the pipeline. The deeper the pipeline the more important it is to have an accurate branch predictor.

## Predictors
For a typical sample instruction pipeline below:
`Fetch -> Read/Decode -> ALU -> Memory Access -> Write the Registers`

### none-predictor
**None-predictor** does not fetch instruction until it is know in `Decode` stage for non-branch inst, or it is decided taken or not in `ALU` stage.
-	Every branch costs 3 cycles.
-	Non-branches cost 2 cycles.

### not-taken predictor
**Not-taken-predictor** predicts and just fetches next instruction:
- Every branch costs 1 or 3 cycles. (depends on the actual taken/not taken result in `ALU` stage).
- Every non-branch inst costs 1 cycle. (because it is not branch, it does not jump on PC, insts is just executed normally in the pipeline)
	
### BTB PC predictor
Model: $$PC_{next}=f(PC_{now},\;history[PC_{now}])$$
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

### direction predictor
**Direction Predictor** uses a branch history table (**BHT**) to first determine if branch is taken or not before BTB. Steps:
1. Use LSB (least significant bits) of PC to index BHT.
2. BHT maps LSB bits to 1 bit that is `{0: not taken and PC++, 1: taken and go to BTB}`.
3. Similar to BTB, if mispredict, update to BHT. ![[BHT.png]]
The problem with 1-bit predictor is that when the not taken and taken branch insts are mixed in program. To solve this, there's a 2-bit predictor.

-	**2-bit predictor**
Enhanced direction predictor to predict branch taken or not.
	- `00`: strong not-taken
	- `01`: weak not-taken
	- `10`: weak taken
	- `11`: strong taken
	The predictor changes weak bit first when facing misprediction, reducing frequent updates that results in high misprediction rate in frequent taken/not taken switches. 
	
### history-based predictor
**history based predictor** predicts branch taken or not based on last two actuals.
	
- 1-bit history with 2-bit counter
`1 bit history | 2 bit counter` This works well in not taken and taken branch insts interchange pattern: `(not taken, not taken, taken)*`
![[hist_based_predictor.png]]
	
- 2-bit history with 2-bit counter
Works well with $(NNT)^*$  (repeat (not taken, not taken, taken) ) pattern, or $(NT)^*$
	
- n-bit history predictor with 2-bit counter
It will predict all patterns of $length \leq n+1$. But cost ($n+2*2^n$) bit per entry. This can be needed in loops that's long $(N..NT)^*$ pattern.

### history based with shared counter predictor
- #### PShare
Private history (each branch inst has its own history bits pattern). Shared counters (between all branches) - good for small loops and predictable short patterns.
Bits cost much lower than n-bit predictor with 2-bit counters.
![[history_with_shared_counter_predictor.png]]
- #### GShare
Global history and shared counter - good for correlated branches.

### Tournament predictor
Use a 1-bit meta-predictor to select `{GShare, Pshare}`;
![[tournament_predictor.png]]

### Hierarchical predictor
Similar to Tournament Predictor.
- Update OK predictor on each decision
- Update **expensive** good predictor if OK predictor not good.

### Return Address Stack (RAS)
Have a small table in stack to store updated address of predicted inst for function `RET` inst.

#### But how to know if it's a `RET` inst or not?
-	Predictor
Have a table store history PC which are `RET`.
- **Predecode**
When fetch inst from mem to cache, predecode it to add an additional bit for this inst to indicate `RET` or not `RET`.

## Avoid branch prediction
See [[Computer Architecture|Predicate]]