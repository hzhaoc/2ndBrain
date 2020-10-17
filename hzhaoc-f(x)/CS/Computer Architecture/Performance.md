Perspectives to think about computer architecture:
-	Performance
-	Energy efficiency
-	Cost

## Common Metrics
-	Latency (start -> done)
-	Throughput (# / second )
-	$Speedup_{x:y}$ = $\frac{latency_y}{latency_x}$ =$\frac{throughput_x}{throughput_y}$ 
	-	If speed up part of the program:
	$speedup_{total}=\frac{1}{(1-a)+\frac{a}{speedup_{a}}}$
	where $a$ is % of **execution time** of the program sped up.
## Benchmark
### Standard
- SPEC
- ...
### Benchmark performance metrics
- (geometric) Average execution time
- CPU time = $\sum{(\frac{instructions}{program} * \frac{cycles}{instruction})} * \frac{time}{cycle}$
number of instructions per program is affected by algorithm, compiler, instruction set;
cycles per instruction are affected by instruction set, processor design;
lock cycle time is affected by processor design, circuit design, transistor physics.