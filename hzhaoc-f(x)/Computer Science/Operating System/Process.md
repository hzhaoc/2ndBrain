# Basic
- CPU has register that has state information for a process.
- When a process starts, a PCB (process control block) is created to monitor and update process states.
- CPU does context switch from one process to another process based on register state information like PCB. disadvantage: 
	- 1. Cost of loading and restoring instructions 
	- 2. Cold cache or cache misses. (cache is read and written much faster than memory)
- CPU scheduler (algorithm) chooses next ready process and dispatches it to CPU and does context switch, before this OS preempts CPU to interrupt current executing process.

# IPC
Processes interact through IPC (inter-process communication) mechanism. Two ways. 
- 1. Kernel OS creates a buffer channel between two processes. 
	- Pros: OS manages IPC. 
	- Cons: Overheads. To transfer data between processes in buffer channel, data need to be copied into buffer first and then copied into another process. 
- 2. OS creates a shared channel directly between two processes. The channel maps virtual addresses between two processes so one can access data to another process through the channel. 
	- Pros: OS out of control. 
	- Cons: No API interface. More errors.
## Requires sync
- Mutex
- Message queues  (send/recv)
- semaphores (binary)
## Message passing
-  e.g. pipes, message queues
-  API: sockets
## Memory-based IPC
- Shared buffer
	- OS out of the way
	- API
		- Sys V – segment shared memory
		- POSIX
		- Mapped files
		- Android ashmen
	- Sync
		- mutex
		- message queue
		- semaphore
## Higher-level semantics
- Files, RPC (remote process control, more than one channel)
## message  buffer vs shared memory
message buffer copy data; shared memory has overhead to map virtual addr to  shared mem