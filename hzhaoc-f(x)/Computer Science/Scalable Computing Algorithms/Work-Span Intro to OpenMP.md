# Shared Memory Addressing & OpenMP
Explicit parallel programming requires specification of parallel tasks along with their interactions. These interactions may be in the form of synchronization between concurrent tasks or communication of intermediate results. In shared address space architectures, communication is implicitly specified since some (or all) of the memory is accessible to all the processors. Consequently,** programming paradigms for shared address space machines focus on constructs for expressing concurrency and synchronization along with techniques for minimizing associated overheads**. In this chapter, we discuss shared-address-space programming paradigms along with their performance issues and related extensions to directive-based paradigms.

Shared address space programming paradigms can vary on mechanisms for data sharing, concurrency models, and support for synchronization. Process based models assume that all data associated with a process is private, by default, unless otherwise specified (using UNIX system calls such as shmget and shmat).

### OpenMP: a Standard for Directive Based Parallel Programming
> ...APIs such as Pthreads are considered to be low-level primitives. Conventional wisdom indicates that a large class of applications can be efficiently supported by higher level constructs (or directives) **which rid the programmer of the mechanics of manipulating threads**. Such directive-based languages have existed for a long time, but only recently have standardization efforts succeeded in the form of OpenMP. OpenMP is an API that can be used with FORTRAN, C, and C++ for programming shared address space machines. OpenMP directives provide support for concurrency, synchronization, and data handling while obviating the need for explicitly setting up mutexes, condition variables, data scope, and initialization.

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
