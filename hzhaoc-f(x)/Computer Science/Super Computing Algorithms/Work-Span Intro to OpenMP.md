# Shared Memory Addressing & OpenMP
Explicit parallel programming requires specification of parallel tasks along with their interactions. These interactions may be in the form of synchronization between concurrent tasks or communication of intermediate results. In shared address space architectures, communication is implicitly specified since some (or all) of the memory is accessible to all the processors. Consequently,** programming paradigms for shared address space machines focus on constructs for expressing concurrency and synchronization along with techniques for minimizing associated overheads**. In this chapter, we discuss shared-address-space programming paradigms along with their performance issues and related extensions to directive-based paradigms.

Shared address space programming paradigms can vary on mechanisms for data sharing, concurrency models, and support for synchronization. Process based models assume that all data associated with a process is private, by default, unless otherwise specified (using UNIX system calls such as shmget and shmat).

### OpenMP: a Standard for Directive Based Parallel Programming
> ...APIs such as Pthreads are considered to be low-level primitives. Conventional wisdom indicates that a large class of applications can be efficiently supported by higher level constructs (or directives) **which rid the programmer of the mechanics of manipulating threads**. Such directive-based languages have existed for a long time, but only recently have standardization efforts succeeded in the form of OpenMP. OpenMP is an API that can be used with FORTRAN, C, and C++ for programming shared address space machines. OpenMP directives provide support for concurrency, synchronization, and data handling while obviating the need for explicitly setting up mutexes, condition variables, data scope, and initialization.
# Message Passing & MPI
##### principals of message passing
The logical view of a machine supporting the message-passing paradigm consists of p processes, each with its own exclusive address space. Instances of such a view come naturally from clustered workstations and non-shared address space multicomputers. There are two immediate implications of a partitioned address space. First, each data element must belong to one of the partitions of the space; hence, data must be explicitly partitioned and placed. This adds complexity to programming, but encourages locality of access that is critical for achieving high performance on non-UMA architecture, since a processor can access its local data much faster than non-local data on such architectures. The second implication is that all interactions (read-only or read/write) require cooperation of two processes – the process that has the data
and the process that wants to access the data. This requirement for cooperation adds a great deal of complexity for a number of reasons. The process that has the data must participate in the interaction even if it has no logical connection to the events at the requesting process. In certain circumstances, this requirement leads to unnatural programs. In particular, for dynamic and/or unstructured interactions the complexity of the code written for this type of paradigm can be very high for this reason. However, a primary advantage of explicit two-way interactions is that **the programmer is fully aware of all the costs of non-local interactions**, and **is more likely to think about algorithms (and mappings) that minimize interactions**. Another major advantage of this type of programming paradigm is that it can be efficiently implemented on a wide variety of architectures.

The message-passing programming paradigm requires that the parallelism is coded explicitly by the programmer. That is, the programmer is responsible for analyzing the underlying serial algorithm/application and identifying ways by which he or she can decompose the computations and extract concurrency. As a result, programming using the message-passing paradigm tends to be hard and intellectually demanding. However, on the other hand, properly written message-passing programs can often achieve very high performance and scale to a very large number of processes.

### MPI: the message passing interface
MPI defines a standard library for message-passing that can be used to develop portable message-passing programs using either C or Fortran. The MPI standard defines both the syntax as well as the semantics of a core set of library routines that are very useful in writing message-passing programs.

# considerations for Design Parallel Algorithms
### Automatic
compiler finds any possible parallelization points

### Manual
programmer finds any possible parallelization points
1. Determine if the problem is one that can be solved in parallel.
2. Identify Program Hotspots
3. Identify Bottlenecks
4. Identify Inhibitors to Parallelism
5. If possible look at other algorithms to see if they can be parallelized.
6. Use parallel programs and libraries from third party vendors.

##### partitioning
Divide the tasks to be done into discrete chunks.There are two methods for partitioning:
1. Domain Decomposition
The data is decomposed. Then each task works on a portion of the data.

2. Functional Decomposition
The problem is broken into smaller tasks. Then each task does part of the work that needs to be done. In functional decomposition the emphasis is on the computation, rather than the data.

Examples of Functional Decomposition
1. Ecosystem modeling
2. Signal processing
3. Climate modeling

##### communications
Which tasks need to communicate with each other. If communication is needed between processes
- message passing (explicit) or shared address spacing (implicit)
- synchronous or asynchronous
- scope
	- point to point
	- collective (data sharing between two or more tasks)

##### synchronization
There are 3 kinds of Synchronization:
- barrier
- lock/semaphore
- synchronous communication operations e.g. send & recv

##### load balancing
keep all tasks computing volume even, so no bottleneck.
