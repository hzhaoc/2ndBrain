# Example
### 2-SAT
- input: 
	- $n$ Boolean variables $x1,x2,...,xn$.
	- $m$ clauses of $2$ 
	- example clause: $xi \ or \ !xj$)
- output:
	- True if there's an assignment that satisfies all clauses
	- False if the opposite.

##### approach 1: reduce to SCC
Notice that for each clause $(x1 \ v \ x2)$, it can be represented in a graph as $(-x1->x2)$ and $(-x2, x1)$, then we only need to run an algorithm to find all [[SCC]]s, and check if there are $xi$ and $-xi$ that are in same SCC: if True, the 2SAT clauses are unsatisfiable;  else satisfiable. (Why?).

This algorithm is Fast and linear in time.

##### approach 2: backtracking
##### approach 3: local search
- repeat $\log_2{n}$ times:
	- choose random initial assignment:
	- repeat $2n^2$ times:
		- if current assignment satisfies all clauses, halt and report
		- if not, pick one arbitrary unsatisfied clause, and randomly flip one of its variable

polynomial run time.
produce a satisfying assignment with probability >= 1 - 1/n