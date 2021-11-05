This topic is based on [[IPC#Message Passing|Message Passing]] communication.

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

##### A Pseudo Code API for Collectives
A collective is an operation that must be executed by all processes.
- **Reduce**: 
	- tree based
		- **T(n) = αlogP + βnlog P** using tree based / divide and conquer.
		- ![[network reduce.png|400]]
		- ```c++
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
	- bucketing reduce scatter -> gather
		- **T(n) = αP + βn**
		
```c++
reduce(A_local[1:n], root)
```
- **Broadcast**: 
	- reverse reduce: **T(n) = αlogP + βnlog P**
	- scatter + all-gather (bucketing): **αP + βn**
		- ![[network broadcast as scatter + allgather.png|250]]
```c++
//T(n) = (α + βn)log P
broadcast(A_local [1:n], root)
```
- **Gather**
	- one node collects all pieces, each from a different node
	- reverse scatter, $T(n)=αlogP+βn$
```c++
gather(In[1:m], Out[1:m][1:P], root)
```
- **Scatter**: reverse of gather
	- naive scatter:  $T(n)=αP+βn$
		- ![[distri mem naive scatter algo.png|300]]
	- If we divide and conquer this scatter, new time is $T(n) = αlogP + βn ((P − 1 ) / P )=αlogP+βn$
		- ![[scatter divide and conquer.png|450]]
```c++
scatter(In[1:m][1:P], root, Out[1:m])
```
- **All-gather**: 
	- **gather -> broadcast**
		- this is slow when n is large. ok when n is small
	- **bucketing**: when n is large, have each process send its piece to its neighbor in each iteration and go all the way down. this can be down in parallel.
		- T(n = mP) = (α + βn/P)(P − 1) ≈ αP + βn
		- αP is sub-optimal, βn is optimal
```c++
allGather(In[1:m], Out[1:m][1:P])
```
- **Reduce-scatter**
	- reduce and then scatter
	- reverse of all-gather; T = αP + βn
```c++
reduceScatter(In[1:m][1:P], Out[1:m])
```
- **All-reduce**
	- reduce-scatter -> all-gather. 
	- T(n = mP) ≈ αP + βn

# MPI basics
##### principals of message passing
The logical view of a machine supporting the message-passing paradigm consists of p processes, each with its own exclusive address space. Instances of such a view come naturally from clustered workstations and non-shared address space multicomputers. There are two immediate implications of a partitioned address space. First, each data element must belong to one of the partitions of the space; hence, data must be explicitly partitioned and placed. This adds complexity to programming, but encourages locality of access that is critical for achieving high performance on non-UMA architecture, since a processor can access its local data much faster than non-local data on such architectures. The second implication is that all interactions (read-only or read/write) require cooperation of two processes – the process that has the data and the process that wants to access the data. This requirement for cooperation adds a great deal of complexity for a number of reasons. The process that has the data must participate in the interaction even if it has no logical connection to the events at the requesting process. In certain circumstances, this requirement leads to unnatural programs. In particular, for dynamic and/or unstructured interactions the complexity of the code written for this type of paradigm can be very high for this reason. However, a primary advantage of explicit two-way interactions is that **the programmer is fully aware of all the costs of non-local interactions**, and **is more likely to think about algorithms (and mappings) that minimize interactions**. Another major advantage of this type of programming paradigm is that it can be efficiently implemented on a wide variety of architectures.

The message-passing programming paradigm requires that the parallelism is coded explicitly by the programmer. That is, the programmer is responsible for analyzing the underlying serial algorithm/application and identifying ways by which he or she can decompose the computations and extract concurrency. As a result, programming using the message-passing paradigm tends to be hard and intellectually demanding. However, on the other hand, properly written message-passing programs can often achieve very high performance and scale to a very large number of processes.

### MPI: the message passing interface
MPI defines a standard library for message-passing that can be used to develop portable message-passing programs using either C or Fortran. The MPI standard defines both the syntax as well as the semantics of a core set of library routines that are very useful in writing message-passing programs.