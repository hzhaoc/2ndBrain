# Type
## FIFO based
## SFJ based - shortest job first
- Possible preemption
- Task execution time can be based on historical average
## Priority based
- Priority inversion: Priority interrupted by mutex. Solution: temporarily boost priority of mutex owner
## Round robin
Time slicing - interleave each thread
-	Pro
	- bring down avg complete and avg wait time
-	Con
	-	overheads of interrupt, schedule, context switch
-	CPU-bound tasks prefer larger timeslice (lower completion time, higher throughput tasks/time
-	I/O-bound tasks prefer smaller timeslice (higher throughput, lower wait time), it hides I/O latency (thread sleeps when waiting for I/O response, this doesn’t happen in memory management)
-	Multiple scheduling queue to separate groups of I/O-intensive and CPU-intensive tasks
-	Example: **Multilevel feedback queue (MLFQ)**
	-	![[multilevel_feedback_q.png]]

# Example
## Linux O(1)
Preemptive, priority-based, constant time to select/add task
- Timeslice: priority go lower -> timeslice go lower
- Feedback: longer sleep (events/user inputs bound, computing intensive) -> priority go higher, timeslice go higher
- Task queue: two arrays: 
	1. Active array of linked lists of tasks, 
	2. Expired array of linked lists of tasks. When an active array priority level timeslice is filled, it goes to expired array. Active array is the array used to pick next task to run. When active array becomes empty, swap active array and expired array.
- Pros
	- constant time to add/select tasks in queue
- Cons
	- not time-sensitive to high priority tasks (with high timeslice), low priority tasks could wait very long (tasks keep added to high priority levels in active array). Expired arrays tasks could also wait very long.
- **Replaced by CFS scheduler since linux kernel 2.6.23**

## CFS
Completely fair scheduler
- Tasks queue: Red-black tree (ordered, balanced)
Ordered by virtual runtime (time spent on CPU)

- Periodically increment virtual runtime on executing task, if running task virtual runtime is larger than leftmost tree node virtual runtime (lowest virtual runtime task), change executing task to the current leftmost node and rebalance the tree

- Virtual runtime progress speed depends on priority and niceness. The higher the priority, the lower the effective rate, the slower the virtual runtime progresses

- Performance: O(1) select task, O(logn) add task

## SMP
Simultaneous multiprocessing. Scheduling on multiple CPUs
- Cache affinity
	- Schedule similar tasks on same CPU to hit hot cache
- Non-uniform memory access NUMA

## [[Thread#Hyper-threading|SMT]]
Simultaneous multithreading. Scheduling for hyperthreading

Co-schedule compute-bound and memory-bound threads
- Pro
	- avoids **Resource Contention** on the same CPU resource pipeline. Hide latency of memory access by context switching in hardware since its time will be much lower than that of memory access.

can use hardware counter to differentiate memory-bound and CPU-bound threads, e.g. cycles per instructions

Mixed CPI in same CPU to co-schedule is good. CPI metric for SMT is good in theory, but in practice, CPI doesn’t vary a lot.

