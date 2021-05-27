# Thread vs. Process
Multithreads in a same process share same virtual to physical address mappings. (**code, data, heap, stack, files**). Each thread has its own stack pointer, registers, program counter, thread ID, etc. (execution context).
![[process_n_thread.png]]
# Basic
## Benefits
1. Parallelization. Speed up dealing with input.
2. Specialization. Hot cache dealing with special tasks.
3. Requires less memory than multi-processes by sharing same addresses. Lower memory management. 
4. Cheaper IPC than multi-processes.
5. Hide latency of I/O operations. (multithreads on single CPU). In graph below, I/O operation latency t\_idle is hidden by t\_ctx\_switch context switch between threads. And context switch among threads is faster than that among processes.
![[multithreads_ctx_switch.png]]
5\. Multithreads on multi-CPUs: Run application concurrently like below
![[multithreads_on_multicpu.png]]
## Adaptive mutex
If a user level thread T1 on a CPU C1 requests a mutex that’s locked by another user level thread T2 on another CPU C2, if the critical section for T2 to execute is short, then OS spins T1 to kernel level thread on C2. If critical section is long, then T1 wait on mutex queue as usual. This is called **adaptive mutex**.
## kernel-level data structure
- Process
	- List of kernel-level thread
	- virtual address space
	- user credentials
	- signal handlers
- Kernel-level threads
	- kernel-level registers
	- stack pointer
	- scheduling info (class, ...)
	- pointers to associated LWP, Process, CPU structures
	- information needed even when a process not running -> not swappable
- Light-weight process (LWP)
	- user-level registers
	- system call args
	- resource usage info
	- signal mask
	- similar to ULT (user-level thread), but visible to kernel
	- not needed when process not running
- CPU
	- current thread
	- list of kernel level thread
	- dispatching & interrupt handling information
	- on SPARC (Scalable Processor Architecture?) dedicated reg == current thread
## Hyper-threading
Architecturally, a processor with Hyper-Threading Technology consists of two logical processors per core, each of which has its own processor architectural state. Each logical processor can be individually halted, interrupted or directed to execute a specified thread, independently from the other logical processor sharing the same physical core.

Unlike a traditional dual-processor configuration that uses two separate physical processors, the logical processors in a hyper-threaded core **share the execution resources**. These resources include the execution engine, caches, and system bus interface; the sharing of resources **allows two logical processors to work with each other more efficiently**, and allows a logical processor to borrow resources from a stalled logical core (assuming both logical cores are associated with the same physical core). A processor stalls when it is waiting for data it has sent for so it can finish processing the present thread. The degree of benefit seen when using a hyper-threaded or multi core processor depends on the needs of the software, and how well it and the operating system are written to manage the processor efficiently.

Multi registers or contexts on the same CPU to support multiple threads in the same CPU. Hardware context switch is much faster; it can even hide memory access idling time.

Need to co-schedule threads on the same CPU by scheduler.
## Model
- Multi-process model
- Multi-thread model
- Event-driven model
	- Pro: 
		- No context-switch cost. One context, one thread, one process, in one even-driven process.
		- Single address space. Smaller memory environment.
		- No synchronization. (like locks/mutex)
	 - Con
		 - A little decrease for locality and less cache hit since model is interleaving events among different request handlers.
	 - ![[even_driven_model.png]]
	 - I/O Blocking
		-	I/O blocking can be solved by **asynchronization calls/operations**. Process/thread makes system calls to kernel OS, and OS obtains all relevant data from stack, and either learns where to return results, or tells caller where to get results later. This way process/thread can continue without waiting for the immediate respond from I/O operations.
		-   Another way to avoid I/O blocking is to add helper thread/process in event-driven model. Event dispatcher passes concurrent possible blocking I/O operations to helpers and move on. It’s called AMPED/AMTED. (asymmetric multi process/thread event-driven). Helper uses pipe/socket-based communication with event dispatcher.        Example: Flash: event-driven web server
		-   

	
