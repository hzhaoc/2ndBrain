### standard form
- n variables $x_1, x_2, ..., x_n$, m constraints
- objective function: max $c1x1 + c2x2 + ... + cnxn$
- s.t. 
	- $a11x1+a12x2+...+a1nxn<=b1$
	- $a21x1+a22x2+...+a2nxn<=b2$
	- ...
	- $am1x1+am2x2+...+amnxn<=bm$
	- $x1>=0$
	- $x2>=0$
	- ...
	- $xn>=0$

In linear algebra view:
- variables x = (x1...xn)
- obj: $C^TX$ where c = (c1...cn)
- s.t. AX <= B where A is (mxn), B=(b1...bm)

**optimum of LP  is achieved at  a vertex of feasible region except if:**
- infeasible
- unbounded

### simplex algorithm
- most widely used
- worst case exponential time
- guaranteed to produce optimal result

algorithm description
- start at x = 0
- look for neighbor vertex with higher objective value then move there and repeat, which higher one to choose is heuristic here, until no neighbor vertexes that have higher objective value, at which time current vertex is optimal

### LP Duality
consider original LP problem:
- variables x = (x1...xn)
- obj: max $C^TX$ where c = (c1...cn)
- s.t. AX <= B, X>=0 where A is $A_{mxn}$, B=(b1...bm)

It's dual LP is m variables, n consntraints
- variables y = (y1...ym)
- obj: min $B^Ty$
- s.t. $A^Ty>=c, y>=0$

##### weak  duality
for feasible points of x, y:  $C^Tx<=B^Ty$
- if we find feasible x, y that  $C^Tx=B^Ty$, then x, y are optimal
- if primal  LP is unbounded, then dual is infeasible
- if dual is unbounded, then primal is infeasible
> if dual LP is infeasible,  primal is either unbounded or infeasible

##### strong duality
- primal LP is feasible and bounded iff dual LP is feasible and bounded
or 
- primal has optimal iff dual has optimal => size of max flow = capacity  of min st-cut

