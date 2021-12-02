##### Loomis and Whitney
In matrix multiply A = BC. Given any sub-block of sA, sB, sC, 
- Volume of $|I| <= √|sA| |sB| |sC|$

### On distributed network
##### 1D network algorithm
Use Block Row Distribution: each node gets n/P rows. In AB=C, A, or B, say B, has to do row shift.
![[distri mem mat mul row distri algo.png|500]]

rearrange code to overlap communication latency: (improve run time by mostly 2)
```c++
let A’[1: n/P] [1:n] = local part of A 
	B’, C’ = same for B, C 

let B’’[1:n/P][1:n] = temp storage 
let rnext ← (RANK + 1) mod P 
	rprev ← (RANK + P ­1) mod P 

for L ← 0 to P-1 do 
	sendAsync (B’ → rnext ) 
	recvAsync (B’’ ← rprev ) 
	C’[:][:] += A’[:][...L…] . B’[...L…][:] 
	wait(*) 
	swap(B’, B’’)
```
- Cost: 
	- $T_{comp} (n,P) = 2τ n^3 / P$
		- τ = time per "flop" (flop means …1 floating point multiply or add)
	- $T_{commu} = αP + βn^2$
		- B’ is the only data communicated. It’s size is n/P words by n columns, so n /P words
		- There are P sends that have to be paid for.

- Efficiency
	- Speedup: $S (n; p) = T_*(n) / T_{1D} (n; p) = P / max(1, 1/2 * α/τ * P^2 /n^3 + 1/2 * β/τ * P/n) = θ(P)$
	- Parallel Efficiency = Speedup/P
		- it is good when it's constant > 0. i.e. when $n = \Omega (P)$
		- if you double nodes, you have to quadruple size of the matrices. Number of floating point computations will increase by factor of 8. If you don't quadruple problem size, you will see diminishing speedup efficiency.

- **Isoefficiency**
	- the value of P that n must satisfy to remain constant parallel efficiency. in the example it is $n = \Omega (P)$
	- **measuring the scalability of parallel algorithms and architectures**

##### 2D network algorithm
each node in mesh responsible for its corresponding block multiplication. trip by strip, each trip needs to be broadcast
![[2d network mat mul algo.png|500]]

- communication time
	- ![[2d network mat mul tcomm.png|400]]
	- mesh is more scalable than linear network for matrix multiply
		- ![[2d network mat mul tcomm efficiency.png|200]]
		- The bucket is slightly worse than the tree, it trades a higher latency cost for a lower communication cost.

##### beyond 2D - lower communication bound
$T (n; p) = a * √P + b * n^2 √P)$