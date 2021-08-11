Synchronization requires the use of locks and barriers. This lesson discusses synchronization as well as various locks and barriers. Check [[Synchronization]] as well

### Mutual Exclusive Synchronization
Thread A and Thread B are executing programs. If the threads both modify the same memory location, the order of the modifications is important. Thus the need for synchronization. 

Atomic Code Sections - these are sections of code that must be executed completely, one at a time. 

Mutual Exclusion - a type of synchronization used for atomic sections of code. Also called a lock. Before entering a critical section, a lock must be implemented. If the lock is held by a core, other cores that want to use the lock have to wait (or spin) until the lock is free. The lock is freed at the end of the critical section. Locks force mutual exclusion. **Locks are just locations in shared memory.**

##### Lock Synchronization
Checking and acquiring a lock must be atomic, otherwise two or cores could hold the lock at the same time, defeating synchronization

- **Implementing Lock()**
1. The lock is checked.
2. If the lock is free, acquire it. 
	1. how to make sure only one thread gets the lock?  LAMPORT's bakery algorithm: expensive; Special **atomic read/write instructions.**
3. If the lock is not free, spin until the lock is free.
4. If the lock is held by the core, unlock it.

An instruction that both reads and writes to memory is required to implement lock().

##### Atomic  instructions
3 Main Types of Atomic Instructions
1. **Atomic Exchange** - the contents of a register and memory location are swapped. 
	- cons: 
		- it continues to swap while waiting to acquire the lock.
		- strange inst
2. **Test and Write** - test the lock before trying to acquire it. If the lock is free, it can be acquired. If the lock is not free, don’t try to write to it. This method corrects the drawback of the Atomic Exchange. 
	-	cons: 
		-	this is a strange instruction, it is neither a store or load. Atomic read/write in the same instruction is bad for pipelining.
3. **Load Linked / Store Conditional (LL/SC)** 
	- inked Load - behaves like normal load but also saves the address from which it loaded to a hidden "link register".
	- Store Conditional - checks first if the computed address == the one in link register. 
		- yes? normal store to that register address, return 1
		- no? return 0
		- cons:
			- same as Test and Write? it does a lot of actual writes (from store instructions) and in Write-Invalidate protocol, it does lots of invalidation of other cores, or in write-update protocol, it does a lot of actual slow memory writes.

##### how is LL/SC together atomic? 
for the example code below:
```
LL R1, lockvar
SC R2, lockvar
```
SC fails if it snoops a write on bus to lockvar, and it will set link register address = 0 which makes the condition "addr in SC inst == addr in link register" returns False and the SC will not proceed. 

If the code is simple, locks are not needed, the LL/SC can be used directly

##### Locks and Performance
If cores are waiting on a lock, the energy spent spinning is quite high and it overloads the bus. When the bus is overloaded with cores checking lock availability even the core that has acquired the lock is slowed down. 

to improve, use **Test and Atomic Op Lock**.  It waits for lockvar to become free using a normal read, when it becomes free, do an Exchange. This will reduce the bus traffic, only the cache is checked

![[Test and Atomic Op Lock.png|500]]

### Barrier Synchronization
A barrier makes sure all the threads wait for the completion of a task before allowing any to go  past the barrier.

Two variables are required for a barrier:
1. A counter to count the number of threads as they arrive at the barrier.
2. A flag that is set when the number of threads at the barrier equals the number of threads required.

##### Simple Barrier Implementation
![[simple barrier sync.png|500]]

**This simple barrier implementation doesn’t work more than once** because there's one deadlock situation when Core A and B reach the barrier and Core B first reset count and release, while Core A is slow and cannot see release == 1 before it changed back to 0 (see above graph), then the second barrier will never be crossed as the count will never equal to total again, thus the deadlock

##### Reusable Barrier
core idea is to flip the release condition for neighbor barriers.
![[reusable barrier.png|500]]