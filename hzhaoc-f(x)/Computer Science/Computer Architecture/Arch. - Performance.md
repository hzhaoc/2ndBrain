Perspectives to think about computer architecture:
-	Performance
-	Energy efficiency
-	Cost

Only consistent and reliable measure of performance is** execution time of real programs**.

## Common Metrics
-	Latency (start -> done)
-	Throughput (# / second )
-	$Speedup_{x:y}$ = $\frac{latency_y}{latency_x}$ =$\frac{throughput_x}{throughput_y}$ 

## Benchmark
### Standard
- SPEC
- ...
### Benchmark performance metrics
- (geometric) Average execution time
- $$CPU \ time \ = \ \sum{(\frac{instructions}{program} * \frac{cycles}{instruction})} * \frac{time}{cycle}$$
	-	insts #:	algorithm, compiler, **instruction set**;
	-	CPI:	**instruction set**, **processor design**;
	-	clock freq:   **processor design**, circuit design, transistor physics.

#### Amdahl's Law:
$$Overall \  Speedup = \frac{1}{(1- P) + \frac{P}{S}}$$
where
$P$ is part of the program execution **time** (not instructions) that is enhanced
$S$ the speedup for that part