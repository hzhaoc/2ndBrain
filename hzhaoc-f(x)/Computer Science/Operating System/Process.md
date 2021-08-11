# Basic
- CPU has register that has state information for a process.
- When a process starts, a PCB (process control block) is created to monitor and update process states.
- CPU does context switch from one process to another process based on register state information like PCB. disadvantage: 
	- 1. Cost of loading and restoring instructions 
	- 2. Cold cache or cache misses. (cache is read and written much faster than memory)
- CPU scheduler (algorithm) chooses next ready process and dispatches it to CPU and does context switch (**this happens when processor/CPU resources do not cover processes existing at one time, so we need to allocate physical CPU resources**), before this OS preempts CPU to interrupt current executing process.
	-  preempt: interrupt current process and save context
	-  schedule: run scheduler to choose next process
	-  dispatch: context switch to the next chosen process

# CPU scheduler 
choose from a ready queue of processes and by some algorithm schedule next process from the queue to run
### with I/O
![[process with IO.png|450]]

# Address Space
##### Virtual Memory for a process
![[process_addr_space.png|400]]
