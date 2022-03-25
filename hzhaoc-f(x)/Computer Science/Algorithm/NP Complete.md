### "Complete"
Given a set of problems $C$, a problem $a$ is $C-Complete$ iff:
- $a$ is in $C$
- all other problems in $C$ can be poly-time reduced to $a$. In other words, if there's a solution to $a$, other problems can be solved based on the solution plus poly-time transfer. If the solution is poly-time solvable (in a deterministic Turing Machine), then all other problems will be poly-time solvable. Thus this solution to $a$ which is $C-complete$ will be a universal solution to all members in $C$.

### NP
By definition, a binary decision problem is in the set of Non-deterministic Polynomial (in short, **NP**), iff:
- the provided answer can be **verified** by a deterministic Turing Machine in polynomial time (what we considered "quick")
- or, equivalently, the provided  answer can be **solved** by a non-deterministic Turing Machine in polynomial time.

### NP-hard
A problem is NP-hard iff:
- any other problem in NP can be poly-time "reduced" (it may actually increase program runtime complexity) to this problem. In other words, any NP problem cannot be harder than this NP-hard problem, or this NP-hard problem is as hard as any other NP problem.

Note: halting problem is NP-hard, but halting problem is NOT in NP.

### Halting problem
Halting problem is whether there exists an algorithm that, given a program and an input, correctly decides if the program will halt. 
- It is NP-Hard - a random NP problem $a$ can be poly-time reduced to a halting problem by having a program $p$ that tries to solve $a$ in a non-deterministic way, and if it solves, halts; otherwise keep running. This transfer is obviously poly-time. And the problem then is transferred to design an algorithm, given $p$, return whether it will halt or not, which is a halting problem.
- It is NOT in NP - halting problem has been proven to be undecidable. [Proof of decidability](https://cs.stackexchange.com/a/65406).  **(I leave doubt to the infinite nest of hypothetical program in that proof trial. Is an infinite nested program sufficient to induce ALL programs follow same rule?)**

### NP-Complete
A problem is NP-complete (Non-deterministic Polynomial Complete) iff:
- the problem is in NP.
- the problem is NP-hard. 

### N=NP?
this notorious question states that if there's a polynomial-time deterministically solvable algorithm / solution to an NP-Complete problem, then any NP-complete problem can be solved deterministically in poly time using this algorithm.

Most believe ("widely conjectured"), yet not proved, $N\neq{NP}$. That is, there's no such polynomial-time deterministically solvable algorithm to solve any NP-Complete problem. This leads that, empirically, if one can not design a poly-time algorithm from common solutions such as greedy, DP, divide and conquer, or any data structures such as disjoint set, hash table, array, linked list, tree, heap, etc, one should consider probability of NP, by proving some NP problem can be poly-time deduced to the problem one is trying to solve.

### Strategies for NP-Complete problems
- identify computationally tractable special cases
- heuristics but not guaranteed to be correct (typically Greedy or DP)
- exponential time yet better than brute-force search

### Examples
##### Traveling Salesman Tour
- [[Dynamic Programming#Traveling Salesman Tour|DP with correctness]]
- Greedy Heuristic
```python
def TSP_heuristic(cities, n):
	"""
	a heuristic greedy approach
	start from an arbitrary city (like 0), repeatedly visit nearest city until all citieis are visited 
	"""
	city, sum_dist, visited = cities[0], 0, {0} # start at city 0
	while True:
		end, nxt_min = 1, float("inf")
		for i, city_nxt in enumerate(cities): # explore nearest neighbor
			if i not in visited:
				end = 0
				_d = _dist(city, city_nxt)
				if _d < nxt_min:
					nxt_min = _d
					nxt_idx = i
		print(len(visited))
		if not end:
			visited.add(nxt_idx)
			city = cities[nxt_idx]
			sum_dist += nxt_min
		else:
			break
	return sum_dist + _dist(cities[0], cities[nxt_idx])

def _dist(city1, city2):
	x1, y1 = city1
	x2, y2 = city2
	return ((x1-x2)**2 + (y1-y2)**2)**0.5
```
##### Knapsack problem
- Input: $n$ items. Each has a positive value $v_i$,  and a size  $w_i$. Also, knapsack capacity $W$.
- Goal: subset $S \in {1,2,...,n}$ that maximizes $\sum_{i\in S}v_i$
- Cons.: $\sum_{i\in S}w_i\leq{W}$ 
- Approach: sort item by ratio of $v_i/w_i$, pack items in order. You can also have another candidate that selects max value of one item. This guarantees at least $50%$ of optimal solution. Note if max $w_i=x$, this heuristic result is at least good as $1-x$ of optimal result. 


