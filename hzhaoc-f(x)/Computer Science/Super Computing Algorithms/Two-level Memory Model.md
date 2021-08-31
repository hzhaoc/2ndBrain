# Two-Level Memory Model
key take-away:  caches managed by hardware itself are fast, but not sufficient, therefore we need algorithms for more efficient slow-fast memory transfers.

### notation
- Q: number of slow-fast memory transfers
- L: block transfer size
- Z: fast memory size
- n: number of elements in slow memory to operate on

## A First Basic Model
To find a locality aware algorithm we need a machine model - will be using a variation on the von Neumann model.  

von Neumann Model:
- Has a sequential processor that does basic compute operations
- Processor connects to a main memory - nearly infinite but really slow
- Fast memory - small but very fast, size = Z ... measured in number of words

Rules:
1. The processor can only work with data that is in the fast memory, known as the local data rule.
2. When there is a transfer of data between the fast and slow memory, the data is transferred in blocks of size **L**, known as the block transfer rule. In this model you may need to consider data alignment 

Costs: The model has two costs associated with it:
1. Work. W(n) == the # of computation operations. (How many operations will the processor have to perform?)
2. **Data transfers, Q(n;Z;L) == # of L-sized slow-fast transfers **(loads and stores). The number of transfers is dependent upon the size of the cache and block size. This will referred to as **Q** and be called the I/O Complexity. 
	- Example: Given an array of size **n**, sum its elements. The processor needs to do at least n-1 additions, W(n) ≥ n-1 additions = Ω(n). For memory transfers → you need to make at least one pass through the data. This can be considered the lower bound on transfers: Q(n,Z,L) ≥ ceiling(n/L) transfers = Ω(n/L). (The ceiling takes into account any partial transfer if n/L is not an integer). Note the equation does NOT depend on Z, the size of the cache - because you are touching each data only once, so the size of the fast memory does not matter. Reduction does not reuse data -- this is BAD!

- Q for sorting algorithm
$Q(n;Z;L) = \Omega(\frac{(n/L)\log(n/L)}{\log(Z/L)})$. **Why?**

- Q for matrix multiplication
$Q(n;Z;L) = \Omega{(n^3/(L\sqrt{Z}))}$. **Why?**

## Algorithm Design goals
- **Work optimality**.  two-level memory model should do asymptotic work as the best serial/sequential RAM model
$$w(n)=\Theta{(w_*(n))}$$
- **High Computational Intensity**.  (do NOT sacrifice work optimality for this!). This metric measures the inherent locality of an algorithm.
$$I(n;Z;L)=\frac{operations}{words}=\frac{w(n)}{L*Q(n;Z;L)}$$

### performance
suppose 
- $\tau=\frac{time}{operation}$ (time per unit of computation operation)
- $\alpha=\frac{time}{word}$ (amortized time per word in slow-fast memory transfer)

then 
- $T_{comp}=\tau w$
- $T_{mem}=\alpha LQ$
- $\max (T_{comp},\  T_{mem})_{\text{perfect overlap}}\leq T_{exe} \leq (T_{comp}+T_{mem})_{\text{no overlap}}$

with refactoring
- $T_{exe}\geq \tau w(1+\frac{\alpha / \tau}{W/LQ})$
	- $\alpha / \tau$ is hardware dependent, so-called "**machine balance**". Denote it $B$. machine balance usually increases in trend, due to more improvement on microprocessor than on memory (multi-core, etc.)
	- $W/LQ$ is computational intensity described above (algorithm dependent). Denote it $I$. 

then
- $T_{exe}\geq \tau w(1+\frac{B}{I})$

if we normalize this performance
- $R\leq \frac{\tau w_*}{\tau w(1+\frac{B}{I})}=\frac{w_*}{w}\min (1, I/B)$ where $w_*$ is best serial RAM model's operations. 

we can see that $R$ is capped when $I=B$ which means 
- when $I<B$, algorithm is memory-bound
- when $I>B$, algorithm is compute-bound

##### more..
The intuition from *energy & time efficiency analysis and actual testing*[^1] is, as intensity increases, 
- time efficiency reaches optimal faster than energy efficiency
- when time efficiency just reaches its optimal at $I=B_{time}$, energy efficiency is at roughly half.
- optimal energy efficiency implies optimal time efficiency; optimal time efficiency does not
- balance gap is because $B_{time}>B_{energy}$, due to "constant power and other microarchitectural inefficiencies".

Check the actual paper for more details.
![[io model balance gap.png|700]] ![[io model balance gap on actual systems.png|600]]

[^1]: Jee Whan Choi, et al, A roofline model of energy, 2012.05