# Two-Level Memory Model
key take-away:  caches managed by hardware itself are fast, but not sufficient, therefore we need algorithms for more efficient slow-fast memory transfers.

### notation
- **Q**: number of slow-fast memory transfers
- **L**: block transfer size
- **Z**: fast memory size
- **n**: number of elements in slow memory to operate on

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

## IO Avoiding Algorithm
Continue analysis for several common IO algorithms:
##### $Q$ (transfers) for merge sort
$$Q(n;Z;L) = \Omega(\frac{(n/L)\log(n/L)}{\log(Z/L)})$$ 
> analysis:
> - Phase 1: for each chunk of fast memory of total $n/Z$ chunks, do sort, takes $ZlogZ$ comparisons, and $Z/L$ transfers. 
>   - total transfer: $n/L$. 
>   - total comparison: $nlogZ$
> - Phase 2: two-way merging. for each sorted chunk of size $Z$ in slow memory, read them into fast mem, and merge two chunks into a bigger sorted chunk, then output. this has $log(n/Z)$ steps. At each step $k$ there's $(n/z)*(1/2)^k$ number of $z^k$ size chunks, 
>   - total transfers: $(n/z)*(1/2)^k*(z^{(k+1)}/L) = 2\frac{n}{L}\log\frac{n}{Z}=O(\frac{n}{L}\log\frac{n}{Z})$ 
>      - (in each merge, you need read two chunks from slow to fast and write back same size.). 
>   - total comparisons: $n\log\frac{n}{Z}=O(n\log\frac{n}{Z})$
>   
> Summing up:
>  - transfer: $O(\frac{n}{L}\log\frac{n}{Z})$ a bit higher than lower bound
>  - comparison: $O(nlogZ)$
> 
> If we do K-way merging that fully utilizes fast mem size $Z$, then we can reach theoretical lower bound:
> - transfers: $\Omega(\frac{n}{L}\log_{\frac{Z}{L}}{\frac{n}{L}})$
> - comparison: $O(nlogn)$

##### Q for binary search
$$Q(n;Z;L) = \Omega{\frac{\log n}{\log L}}$$
> according to information theory, an array with $n$ binary bits contains $\log n$ information. For each $L$ transfer, you can learn $\log L$ information.
> 
> van emeda boas data layout in fast memory achieves this lower bound: (DATA STRUCTURE MATTERS.)
> - recursively partition a binary search tree by half (equal height) into subtrees, align divided subtrees linearly in consecutive memory space (each base subtree must fit into a cache line of course)
> - ![[binary search lower io bound from van emeda boas.png|600]]

##### Q for matrix multiplication
$$Q(n;Z;L) = \Omega{(n^3/(L\sqrt{Z}))}$$ 
- proof 1: 
![[matrix multiply block transfer.png|600]]
- proof 2 from a different divide and conquer algorithm:
	- operations: $O(2n^3)$
	- transfers: $Q(n;Z;L) = \Omega{(n^3/(L\sqrt{Z}))}$
![[matrix multiply divide and conquer.png|600]]

## about Cache oblivious..
the term Cache oblivious refers to an IO algorithm whose $Q$ is irrelevant to cache size $Z$. for example, sum of $n$ size array takes $Q=O(n/L)$. for a counter example, matrix multiplication in block transfer is cache ware.

##### LRU-OPT Competitiveness Lemma
the lemma[^2] says $$Q_{LRU}(n;Z;L)\leq 2Q_{OPT}(n;\frac{n}{2};L)$$ It means that number of transfers for a LRU-based cache can be asymptotically close to number of transfers for an cache with optimal replacement policy but only half of size. 

##### Corollary (Regularity Condition)
$Q_{OPT}(n;Z;L)=O(Q_{OPT}(n;2*Z;L))$. For example, previously we see for matrix multiplication, $Q(n;Z;L) = \Omega{(n^3/(L\sqrt{Z}))}$, when $Z$ doubles, there's only constant factor change of optimal number of transfer.

Once the $Q$ obeys this condition, then the lemma stays.

##### tall-cache assumption
an interesting design assumption of cache where its height (number of cache lines) shall be larger than its width (number of words in a line). this will be helpful when algorithm is related to matrix block transfer. for example, a $b*b$ block transfer requires $Z\geq b*b$

most actual caches, probably except for TLB, are indeed tall.


[^1]: Jee Whan Choi, et al, A roofline model of energy, 2012.05
[^2]: Frigo et al, (FOCS, 1999)