Work-Span model is implemented by a DAG (directed acyclic graph) where each node as a work depends on one another. 

Assume:
1. All processors run at same speed
2. 1 operation work = 1 unit of time
3. no edge cost

Denote:
- total work: $W(n)$
- depth of DAG: $D(n)$
- number of processors: $p$
- total execution time: $T_p{n}$

### Analysis
- $T_p{n}\geq\max \{D(n), \ \ \text{Ceil}(\frac{W(n)}{p})\}$
	- Span Law: $T_p{n}\geq D(n)$
	- Work Law: $T_p{n}\geq\text{Ceil}(\frac{W(n)}{p})$

##### Brent's Theorem
break execution in phases:
- each phase has 1 vertex in critical path (longest path in DAG)
- non-critical path vertex in each phase are independent
- every vertex must appear in some phase

extra denote:
- execution time in $k$th phase: $t_k$
- work in $k$th phase: $w_k$

then:  $$t_k=\text{Ceil}(\frac{w_k}{p})=>T_p=\sum_{k=1}^D{\text{Ceil}(\frac{w_k}{p})}\leq\sum_{k=1}^D\text{Floor}(\frac{w_k-1}{p}+1)=\frac{W-D}{p}+D$$

to sum up: $$\max \{D(n), \ \text{Ceil}(\frac{W(n)}{p})\}\leq T_p\leq{\frac{W-D}{p}+D}$$

##### Speedup
Consider speedup on our DAG parallel algorithm calculated as $$\frac{best\ sequential \ time}{parallel\ time}$$
namely $$S_p(n)=\frac{T_*(n)}{T_p(n)}$$
substitution by previous inequality: $$S_p(n)\leq \frac{p}{\frac{W}{W_*}+\frac{p-1}{W_*/D}}$$

you can clearly see if speedup wants to scale linearly with $p$, this two equation must be met in the scaling inequality:
- work optimality: $$W(n)=O(W_*(n))$$
- weak scalability: $$p=O(\frac{W_*}{D})$$

### basic concurrency primitives
![[basic concur primitives.png|600]]
-  spawn: child thread
-  sync
-  par-for (parallel loop, generate independent child for each iteration)
	-  **if iteration operation is independent of each other, the total span will be $O(logn)$ by divide and conquer, not theoretical $O(1)$ since all iterations can not be spawned all at once.**  See below the assumed implementation for par-for in the course CSE 6220.
	-  ![[par-for implementation.png|550]]

### desiderata for work-span
- work optimality: $$W(n)=O(W_*(n))$$
- "low" span (poly-logarithmic): $$D(n)=O(log^kn)$$

motivation: $\frac{W}{D}=O(\frac{n}{log^kn})$ grows nearly linearly with $n$

##### matrix-vector multiply
- loop1 operation is independent
- loop2 operation is also independent with a temp value
![[work-span matrix mult.png|600]]