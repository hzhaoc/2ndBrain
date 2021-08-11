Memory consistency guards against problematic instruction reordering that destroys synchronization. 

Memory consistency determines the order of accesses by different cores. Memory consistency and sequential consistency go hand-in-hand in ensuring programs execute properly. Without sequential consistency a program execution cannot be guaranteed to have the same outcome with time.

##### Memory Consistency
Coherence defines the order of accesses of threads to the same address. It does not say anything about accesses to different addresses. Memory Consistency defines the order of accesses to different addresses. 

Does order of accesses to different addresses matter?
Yes. Additional ordering restrictions are needed to prevent the incorrect outcomes that can occur in Data Ready Flag synchronization and Thread termination. Consistency ensures the program order is the same as the execution order. especially in OOO processors.

##### Sequential Consistency
The result of any execution should be:
- As if the accesses were executed in-order by each processor
- As if the accesses among different processors were arbitrarily interleaved

> The [sequential consistency](https://en.wikipedia.org/wiki/Sequential_consistency "Sequential consistency") model was proposed by Lamport(1979). It is a weaker memory model than strict consistency model. A write to a variable does not have to be seen instantaneously, however, **writes to variables by different processors have to be seen in the same order by all processors**. As defined by Lamport(1979), sequential consistency is met if "the result of any execution is the same as if the operations of all the processors were executed in some sequential order, and the operations of each individual processor appear in this sequence in the order specified by its program."

##### Simplest Implementation of Sequential Consistency:
- A core performs the next access only when all previous accesses are complete.
- Unfortunately this leads to poor performance.

##### Better Implementation of Sequential Consistency
- A core can reorder loads
- Detect when sequential consistency may be violated and fix it.
	- fix
		-  monitor the coherence traffic produced by other processors. Coherence traffic refers to the load and store commands, especially out of order commands. If there's one consistency violation detected, undo the damage in [[ILP - OOO EXE w Reorder Buffer|reoder buffer]]

##### Relaxed Consistency
> Some different consistency models can be defined by relaxing one or more requirements in [sequential consistency](https://en.wikipedia.org/wiki/Sequential_consistency "Sequential consistency") called relaxed consistency models. These consistency models do not provide memory consistency at the hardware level. In fact, **the programmers are responsible for implementing the memory consistency by applying synchronization techniques.** See more at [Wikipedia](https://en.wikipedia.org/wiki/Consistency_model#Relaxed_memory_consistency_models)


Tell the programmers that they cannot expect sequential consistency for all instances. 
4 types of consistency:
1. RD A -> WR B
2. WR A -> RD B
3. WR A -> WR B
4. RD A -> RD B

When there are situations where program order must be obeyed for above scenarios, use for example MSYNC in x86 for memory consistency. What MSYNC does is that **it ensures all store/write instructions before it are completed before proceeding to following store/write instructions**. It is usually placed after an "acquire" access, like locking, and before a "release" access, like unlocking.

### Data Races and Consistency
Data race: accesses to the **same address by different cores** that are not ordered by synchronization

A data-race-free program cannot create data races. A key property is the program will behave the same in any consistency model. So the program can be debugged in a sequential consistency model, then run on a relaxed consistency model. In a non-data-race-free program anything can happen.

##### consistency models
- sequential
- relaxed (sequential) (key is programmers responsible for implementation synchronization techniques in program to ensure correct order of execution)
	- weak
	- processor
	- release
	- lazy release
	- ...
