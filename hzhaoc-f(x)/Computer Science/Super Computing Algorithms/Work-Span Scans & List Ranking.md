### parallel add scan on Random Access list
- In naive implementation, scans cannot be parallelized because each iteration are interdependent. 
- To think about another way to parallelize: in each iteration, do **reduce** to parallelize pairs of adds. This has O(logn) span. But O(n^2) work. Not work optimal.
- Think about another way below: (**parallel add scan**)
	- recursively add up even indexes so even indexes are presummed.
	- then recursively combine pairs of even and odd indexes so odd indexes are also presummed.
		- work is $O(n)$ ($\theta (2n)$ more accurately)
		- span is $O(log^2n)$
	- ![[parallel scan.png|600]]

### Scan on Quicksort
when doing partition:
- par-for to get flags
- par-for scan to get presums
- par-for to get partitioned array
- `gatherIf(A[:],  F[:])` can be converted to `A[F[:]]`
![[quicksort scans.png|600]]

### Segmented scan
scan by segments of array.
- the `op` operation in the algorithm is associative which is necessary
![[segmented scan.png|550]]

### Scan on Linked-List (Wylie's, non-work-optimal)
If the list to to scanned (do presum, for example) is not a random access array, but a **singly-linked list**.

Scheme:
-  store list as array pool, one for index: value, one for index: next node index
-  iteration:
	-  list ranking -> add scan
	-  pointer jumping (divide and conquer)

This list ranking algorithm shown below does the following:
- in each iteration
	- par-for update rank
		- ![[parallel list ranking  - update rank.png|450]]
		- ranking in each pair that's going to be jump is independent, so can be done in parallel
	- par-for jump (divide & conquer)
- work: $O(mlogm)$
- span: $O(log^2 m)$
![[list ranking algorithm.png|550]]

### Scan on Linked-List (work-optimal)
Scheme:
1. still convert nodes to array pool, then shrink array to size $m=O(\frac{n}{logn})$ to make work $O(mlogm)=O(n)$. 
2. run the previous ranking list scan (assume this is the dominate work)
	- work $O(mlogm)=O(n)$ (accurately it is $O(nloglogn)$, span $O(logn*loglogn)$)
	- span (approx) $O(log^2n)$
3. restore full list

##### the algorithm
1. Initialize ranks:
	- root as 0, other nodes as 1.
2. Random parallel Independent set: a set of non-adjacent nodes
	- randomly assign each node 0 or 1 in parallel
	- flip first 1 to 0 in each consecutive 0 pairs in parallel
	- `gatherif` in parallel
	- work: **O(n).**
	- span: **O(logn)**
	- the independent set size is $1/4$ of original list on average
	- ![[par independent sets.png|500]]
3. Remove the set:
	- push removed nodes' ranks to next in parallel 
	- reconnect remaining nodes (jump) in parallel
4. If remaining list size does not meet the requirement:  $m>O(\frac{n}{logn})$. Go back to **step 2**.
5. If $m=O(\frac{n}{logn})$, do list ranking. Remaining nodes will be correctly ranked.
6. Reverse the process in step 1-4 to correctly rank other nodes. Since each set contraction shrink list to $3/4$ of its original, average number of contractions will be $\Theta (loglogn)$
7. done

### Scan on Postorder tree
##### sequential traverse
![[postorder tree traversal sequential.png|500]]

##### Euler circuit way
1. tree -> list, the Euler circuit
2. mark parent->child sink node as 0, child->parent sink node as 1. (constant time)
3. do add scan on the list. done.
![[euler circuit.png|300]]

### Scan on tree levels
Similar to tree ordering:
1. tree -> Euler circuit
2. parent->child sink node as 1, child->parent node as -1
3. do add scan on the list. done.

##### Euler circuit implementation
- a table like below
- successor function: $s(u_i, v)=(v, u_{(i+1)mod\ d_v})$
- maybe even add direct links for cross edges
![[Euler circuit table.png|500]]