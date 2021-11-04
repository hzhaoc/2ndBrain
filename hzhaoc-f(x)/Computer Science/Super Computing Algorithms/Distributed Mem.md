### A Basic Model of Distributed Memory
Assumptions
- network nodes are fully connected, bidirectionally (so communication between two nodes can happen two way simultaneously)
- two nodes communicate messages one at a time
- cost of communication between two nodes are independent of paths taken in the network graph (Later in lesson this will be discussed)
	- time for communicating **n** words
	- $T=\alpha +  \beta n$
- when there's **k** messages competing for same message channel between two nodes, each with **n** words. this is sequential
	- $T=\alpha + \beta n k$

##### Pipelined message delivery
If two nodes are P nodes away in network, two directly connected nodes has message delivery time of t, then transferring n words between these two nodes needs time
$$\alpha + t(P-2) + tn$$
- first term is software preparation overhead
- second is delay
- third is message size 
- first two terms can be thought of constant

##### Point to Point primitives
- assume SPMD style
- handle ← sendAsync(buf[1:n] → dest)
	- the return does not tell you very much. This is done to allow the programmer theability to decide what to do about a send message: wait for ‘message received’ or make acopy and continue to work.
- handle ← recvAsync(buf[1:n] ← source)
	- return means the message was delivered.
- wait(handle1, handle2, ...) or wait(*)

> Remember every send must have a matching receive
> sendAsync and recvAsync can get trapped in a deadlock depending upon how the wait isimplemented.

##### All-to-One Reduce Pseudocode
![[network reduce.png|400]]

```c++
let s = local value
bitmask ← 1
while bitmask < P do
	PARTNER ← RANK xor bitmask
	if RANK & bitmask then
		sendAsync (s → PARTNER)
		wait(*)
		break //one sent, the process can drop out
	else if (PARTNER < P)
		recvAsync(t ← PARTNER)
		wait(*)
		S ← S + t
	bitmask ← (bitmask << 1)

if RANK = 0 then print(s)
// RANK(Receiver) < RANK(Sender) < P
```

a vector version
- time: $(\alpha + \beta n)logP$
```c++
let s = local value
bitmask ← 1
while bitmask < P do
	PARTNER ← RANK xor bitmask
	if RANK & bitmask then
		sendAsync (s[:] → PARTNER)
		wait(*)
		break //one sent, the process can drop out
	else if (PARTNER < P)
		recvAsync(t[:] ← PARTNER)
		wait(*)
		S[:] ← S[:] + t[:]
	bitmask ← (bitmask << 1)

if RANK = 0 then print(s)
// RANK(Receiver) < RANK(Sender) < P
```

> dual: reduce <-> broadcast
> - broadcast is reverse of such reduce
> 
> dual:  scatter <-> gather
> 
> dual : reduce-scatter <-> all-gather