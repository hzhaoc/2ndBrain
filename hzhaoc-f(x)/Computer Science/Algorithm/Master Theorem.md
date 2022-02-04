When analyzing algorithms, recall that we only care about the asymptotic behavior. Recursive algorithms are no different. Rather than solve exactly the recurrence relation associated with the cost of an algorithm, it is enough to give an asymptotic characterization. The main tool for doing this is the [master theorem](chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/http://cse.unl.edu/~choueiry/S06-235/files/MasterTheorem.pdf).

## Master Theorem
Let $T(n)$ be a monotonically increasing function that satisfies 
- $T(n)=aT(n/b) +f(n)$
- $T(1)=c$

where $a≥1$, $b>1$, $c>0$. 

Iff $f(n)∈Θ(n^d)$ where $d≥0$, then 
- $T(n)=Θ(n^d)$ if $a<b^d$
- $T(n)=Θ(n^dlogn)$ if $a=b^d$
- $T(n)=Θ(n^{log_ba})$ if $a>b^d$

You cannot use the Master Theorem if 
- $T(n)$ is not monotone, ex: $T(n) = \sin n$
- $f(n)$ is not a polynomial, ex: $T(n) = 2T(n/2) + 2^n$
- $b$ cannot be expressed as a constant, ex: $T(n) =T(\sqrt n)$

##### Corollary
If $f(n)∈Θ(n^{log_b a}log^k n)$ for some $k≥0$ then  
$$T(n)∈Θ(n^{log_b a}log^{k+1} n)$$