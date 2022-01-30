Modular arithmetic is a system of arithmetic for integers, which considers remainders from division.
> source: Brilliant.org

### Congruence
For a positive integer $n$, the integers $a$ and $b$ are congruent $\mod n$ if their remainders when divided by $n$ are the same.
e.g. 
$$52 \equiv 24 \mod{7}$$
### Addition
1. if $a+b=c$, then $a \mod N + b \mod N \equiv c \mod N$
2. if $a \equiv b \mod N$, then $a + k \equiv b + k \mod N$ for any integer $k$.
3. if $a\equiv b \mod N$ and $c \equiv d \mod N$, then $a+c \equiv b+d \mod N$.
4. if $a \equiv b \mod N$, then $-a \equiv -b \mod N$.

### Multiplication
1. if $a*b = c$, then $a \mod N * b \mod N \equiv c \mod N$.
2. if $a \equiv b \mod N$, then $ka \equiv kb \mod N$ for any integer $k$.
3. if $a \equiv b \mod N$ and $c \equiv d \mod N$, then $ac \equiv bd \mod N$

### Exponentiation
1. if $a \equiv b \mod N$, then $a^k \equiv b^k \mod N$ for any positive integer $k$

### Division
1. if $\gcd(k, N)=1$ and $ka \equiv kb \mod N$, then $a \equiv b \mod N$.

### Multiplicative Inverses
based on [[Lemmas#Bezout's Identity|Bezout's Identity]], if $a$ and $N$ are integers such that $\gcd(a, N)=1$, then there exists an integer $x$  such that $$ax \equiv 1 \mod N$$
##### [[Lemmas#Extended Euclidean algorithm|Extended Euclidean algo]] to compute modinv
- code from Brilliant.org
```python
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
```

- my code (not tested)
```python
def egcd(r0, r1):
	# extended euclidean algo
	# r0 > r1
	s0, s1, t0, t1 = 1, 0, 0, 1
    x,y, u,v = 0,1, 1,0
    while r1 != 0:
        q = r0//r1
		r0, r1 = r1, r0%r1
		s0, s1 = s1, s0 - q*s1
        t0, t1 = t1, t0 - q*t1
    gcd = r0
    return gcd, s0, t0

def modinv(a, m):
    gcd, s, t = egcd(a, m)  # x, y are bezout coefficients
    if gcd != 1:
        return None  # modular inverse does not exist
    return s
```
