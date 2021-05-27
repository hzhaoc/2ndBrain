# Spinlock 
1. Atomic instructions.
They set a set of instructions to be run in sync.
2. Shared memory processor (SMP)
	- No-write
		- Cache write not allowed, directly write in memory
	- Write through
		- Write both cache and memory
	- Write back
		- Write cache and then memory when that data in cache is evicted
3. Cache coherence (hardware property)
- Non-cache-coherent
	- Write is not allowed
- Cache-coherent -> write-invalidate
	- Software sync same variable in different processes that has shared memory. Same variable update value in one process -> its address is invalidated in another process’ cache line. And it will direct to memory. 
	- Pros: lower bandwidth, only sending address not value; amortized cost, frequent value updates with only one invalidation
- Cache-coherent -> write-update
	- Hardware sync same variable in different processes with shared memory.
	- Pros: update immediately in all processes
4. Atomic instructions in SMP/cache coherence
Atomic instructions bypass caches and directly access shared memory for sync purpose.
- Pros: ordered and synced.
- Cons: memory contention, longer latency (memory > cache)
5. Design of spinlock
- Lower latency (less instructions to acquire lock, i.e. only one atomic instruction)
- Lower delay (less time to acquire lock after waiting, i.e. spin in waiting)
- Fewer contention on bus/inter-connected shared memory
	1. Delay-based spinlock
	2. Queuing/Anderson lock
		-	Pros: one thread acquire lock at a time/no contention
		-	Cons: assumes read-and-increment atomic; N locks
		-	![[anderson_lock.png]]

# Mutex/cond variable
# Semaphore
# Reader/writer lock
# Monitor
# Other: Serializer, path expression, barriers, rendezvous points, optimistic wait-free sync (RCV)