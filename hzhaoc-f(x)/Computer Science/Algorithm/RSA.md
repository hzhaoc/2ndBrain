continue from [[Modular Arithmetic]]


### Fermat's little theorem

if $p$ is prime then for every $1 <= z <= p-1$, $Z^{P-1} \equiv 1 \mod P$ . This is basis of RSY/Cryptosystem. 

### Euler's (generalized) therom
For any N, Z, where $gcd(Z, N)=1$, then $Z^{\phi(N)}\equiv 1 \mod N$, where $\phi{N}$ is number of n from 1 to N which are co-prime to N ($gcd(n, N)=1$)
- for N = p*q (p, q is prime), then $Z^{(p-1)(q-1)}\equiv 1 \mod N$

# RSA
##### Idea
for primes p, q, let N = pq. take d, e where $de \equiv 1 \mod (p-1)(q-1)$, then $Z^{de} \equiv Z \mod N$
here d, e is decryption, encryption key, Z is a message

##### Protocol
1. Bob picks n-bit random primes p & q
	- **how to check random number is prime?**
2. Bob chooses e relatively prime to (p-1)(q-1), let N = pq
3. bob publishes his public key (N, e)
4. bob computes his private key $e$ where $de \equiv 1 \mod (p-1)(q-1)$

Alice wants to send Z to Bob
1. Alice computes $Y=Z^e \mod N$ and send Z

then
1. Bob receives Y
2. decrypt it: $Y^d \mod N = Z$