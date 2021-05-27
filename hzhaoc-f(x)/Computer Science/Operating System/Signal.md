# Interrupts & Signals
## Basic
- Interrupts are events generally outside of CPU, like I/O devices, timers, other CPUs. **Depend on physical platform. Notifications delivered to a CPU.**
- Signals are events triggered by CPU & software running on it. **Depend on OS. Notifications delivered to a process.**
- Both have a unique ID depending on hardware or OS. Can be masked and disabled/suspended/enabled. If enabled, trigger handler (interrupt handler set for entire system by OS, signal handler set on per process basis, by process).
## How interruptions/signals work with thread
- When an interrupt/signal occurred by I/O or OS, OS sends notifications to the relative thread. The program counter on the thread’s execution context points to the start address of the that signal handler and starts the handling routine
- **Deadlocks** can happen if handling routine and thread original execution has the same mutex. 
	- **Top: fast non-blocking**: To avoid this, interrupt/signal is masked by a sequence of binary codes indicates enabled/disabled state of each interrupt/signal. If disabled, signal/interrupts go to **pending** queue, after thread releases the mutex, it changes the interrupt/signal codes to indicate enabled for that interrupt/signal. Then thread starts executing handling code for that interrupt/signal in the pending queue. 
	- **Bottom: arbitrary complex**: Another way to avoid deadlocks is if handling routine has locks, dynamically create a thread for handling routine; this thread can be from pre-created threads pool. This way masks can be all enabled because it’s safe.
- **Native POSIX Threads Library (NPTL)** is 1:1 model. Kernel sees each user level thread information.
- Signals are rare. To optimize, OS updates masks in user level thread, but not in kernel.
- Interrupt masks are per CPU. If masked disabled, hardware will not deliver interrupt to CPU; Signal masks are per execution context, if masked disabled, kernel OS sees mask and will not deliver signal to thread. Interrupts/signals can be set to a single CPU on a multi-core system to avoid overheads and perturbation.
### Types
One-shot vs. real time.