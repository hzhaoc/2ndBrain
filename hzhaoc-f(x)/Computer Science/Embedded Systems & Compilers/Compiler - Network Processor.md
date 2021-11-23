IP Router
- device that performs the network layer forwarding function of the Internet Protocol.

![[IPRouter2.png]]
![[IPHeader.png]]

Network Processor
- ![[NetworkProcessors.png]]
- ![[WhyNetworkProcessors.png]]
- ![[OrganizingResources.png]]

# Dual Bank Problem
In network processor, for ALU instruction, two operands should come from two different banks for parallelization. 

Constraint:
- some variables/registers can not be in different banks
- some can be allocated to different banks, but allocation is imbalanced.

Approach:
- build a **Register Conflict Graph (RCG)** graph where nodes are variables, edges indicate nodes are needed to be in different banks. Also consider Interference Graph for live ranges.
- break odd cycles. From small to big. Only a RCG without odd cycles can be a bipartie graph. Only a bipartie graph has no dual bank problems.
- Bank Assignment can be done in 
	- Pre-Register-Allocation
		- work on virtual RCG 
	- Post-Register-Allocation
		- work on Physical RCG

![[RCG algo.png|600]]

# Register Sharing
Lightweight context switch only stores program counter (PC), to minimize switch overhead. **In lightweight multi-threads environment, no actions of registers saving or storing occur during context switch**. So it is compiler's job to manage register allocations for sharing part, in order to reduce overall register pressure, spill cost, and context switch overhead.

![[reg sharing.png|550]]

When context switch & analyze liveness:
- variables which are not live at the switch are put into Shared Registers
- variables which are not live at the switch are put into Private Registers
- intuitively, more usage of shared registers lead to better and more efficient usage of the registers as a whole

![[reg alloc multithread framework.png|500]]

1. Non-Switch Region
basic blocks divided into regions by switches.
![[non-switch-region.png|500]]
2. Internal Interference Graph: variables not live across NSR
3. Boundary Interference Graph: opposite
![[interference graph with NSR.png|500]]
4. Inter-Thread Register Allocation
- target: spill avoidance
- find solution through live range splitting, calculate cost of `MOV` instruction
- reduce Private Register else or Shared Register until done
![[Inter-Thread Reg Alloc.png|500]]