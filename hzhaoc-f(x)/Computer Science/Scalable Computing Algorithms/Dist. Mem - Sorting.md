From [[Work-Span Comparison-Based Sorting]] we know how to do bitonic sorting by recursively generate bitonic sequence and do bitonic merge.

### Distributed Bitonic Merge
Take this single bitonic merge on 4-node network for example:
- Communication 
	- happens in the first logP iterations (or last $logp$ if it is round-robin/cyclic fashion). Remaining $logn/p$ iterations are all local processing.Time is $T=logp(a+b*n/p)$.  
		- ![[bitonic sort on  network.png]]
	- if it is transpose, Time = $T=a(p-1)+b\frac{n}{p}\frac{p-1}{p}$ (sacrifice a term for b term). Communication time is $T=logp(a+b*n/p)$
		- ![[bitonic sort transpose on network.png]]


> Hypercube or above (like fully-connected) network allows fully concurrent processor message exchange without congestion. 

### Distributed Bitonic Sort
Full bitonic sort communication is $O(alogp+b\frac{n}{p}log^2p)$

### Bucket Sort
1. assuming you know value ranges R = [0, m-1]
2. assuming values uniformly distributed
3. divide R **at even space** into k buckets
4. figure out each value belongs to which bucket
5. sort within each bucket and concatenate the results

Time
1. time to sort each bucket is $O(n/klog(n/k))$
2.total time is $O(nlog(n/k)$ or $O(n)$ if $k=\theta (n)$

### Distributed Bucket Sort
1. each node scan its local elements and decide which element goes where, in parallel. 
2. exchange elements among nodes in all-to-all operation. 
3. each bucket does local sort. 

Time = $O( b*(n/p) + t*(n/p) +(a*p))$

##### with sampling
Bucket Sort has a flaw: data are assumed to be uniformly distributed. What if they are not?

Do a sampling bucket sort:

1. assume number of elements is still equally distributed across nodes
2. sort them locally
3. each node selects a sample of p-1 elements from local sorted list, which should be equally spaced
4. gather samples in root node
5. sort gathered samples in root
6. select p-1 splitters
7. broadcast splitters
8. each node can partition its elements using the splitters
9. then nodes exchange values to hold only its values within range
10. local sort
11. done

Running Time of largest asymptotic function of P is $O(P^2)$ or $O(P^2logP)$. If p is massive, this could be a bottleneck to scalability.
