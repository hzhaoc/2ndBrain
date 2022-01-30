# Bezout's Identity
let $a$, $b$, $d$ be integers such that $\gcd(a, b)=d$, then there exists integers $x$, $y$ such that $ax+by=d$. Moreover, $d$ is the smallest positive integer of linear combinations of $a$, $b$.

a special case is when $a$, $b$ are coprime: $\gcd(a,b)=1$, then $ax \equiv 1 \mod b$, for $\exists \ x \in \mathbb{Z}$. Vice versa. [[Modular Arithmetic#Multiplicative Inverses|Multiplicative Inverse]]

##### [Proof](https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity#Proof)
denote a set $S={ax+by \;|\; x,y \in \mathbb{Z}} \;\&\; ax+by>0$. Obviously, $S$ is nonempty. Thus it has a smallest element, and denote it $s_0$ and $s_0=ai_0+bj_0$. To prove $s_0=d$, it must be proven that $s_0$ is a common divisor of $a$ and $b$, and its the smallest one. 

break down $a$ by $s_0$ with division and denote $a=s_0q+r$, and so $0<=r<s_0$. $r=a-qs_0=a-q(ai_0+bj_0)=(1-qi_0)a+(j_0)b$. Thus $r \in S \cup \{0\}$. Since $r < s_0 = min(S)$, it has to be that $r=0$. Thus $a$ is a divisor of $s_0$, similarly, $b$ is a divisor of $s_0$. 

let $c$ be any common divisor of $a$, $b$ and denote $a=cu$, $b=cv$, so $s_0=ai_0+bj_0=c(ui_0)+c(vj_0)=c(ui_0+vj_0)$. Thus $c$ is a divisor of $s_0$. So $c <= s_0$. So $s_0=\gcd(a, b)=d$

##### Generalizations
if $\gcd(a_1,a_2,...,a_n)=d$, then $\exists x_1, x_2, ..., x_n \in \mathbb{Z}$ such that 
$$d=a_1x_1+a_2x_2+...+a_nx_n$$
- $d$ is the smallest positive integer of this linear form
- every number of this form is a multiple of $d$


# Euclidean Algorithm
a certifying algorithm that efficiently computes $\gcd(a, b)$  for any integers $a$, $b$

step:
- $r_0=a$, $r_1=b$,          let $a>=b$
- ...
- $r_{i+1}=r_{i-1}-q_ir_i$,     $q_i$, $r_{i+1}$ is quotient, remainder of $r_{i-1} / r_i$
- stop if $r_{n+1}$, $\gcd(a, b)=r_n$

### Proof
as $0 <= r_{i+1} < r_i$, series is decreasing, so it will eventually stop at 0. 
as $r_{i+1}=r_{i-1}-q_ir_i$, gcd is same for $(r_{i-1}, r_i)$ and $(r_i, r_{i+1})$. Thus $r_n=\gcd (a,b)$ 

### Extended Euclidean algorithm
extended algorithm that additional to gcd, computes Bezout's coefficients $x$, $y$, such that $ax+by=gcd(a, b)$

step:
- $r_0=a$, $r_1=b$, $s_0=1$, $s_1=0$, $t_0=0$, $t_1=1$         let $a>=b$
- ...
- $r_{i+1}=r_{i-1}-q_ir_i$,     $q_i$, $r_{i+1}$ is quotient, remainder of $r_{i-1} / r_i$
- $s_{i+1}=s_{i-1}-q_is_i$
- $t_{i+1}=t_{i-1}-q_it_i$
- stop if $r_{n+1}$
- $\gcd(a, b)=r_n$
- $s_na+t_nb=r_n$

##### quick proof for Bezout's coefficients
- for $i = 0$ or $i=1$:
	- as $r_0=a$, $r_1=b$, $s_0=1$, $s_1=0$, $t_0=0$, $t_1=1$ we have $as_0+bt_0=r_0$, $as_1+bt_1=r_1$
- it follows by that for any $i > 1$:
	- $r_{i+1}=r_{i-1}-r_iq_i=(as_{i-1}+bt_{i-1})-(as_i+bt_i)q_i=as_{i+1}+bt_{i+1}$
	- thus $s_n$ $t_n$ are Bezout coefficients