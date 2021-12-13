This Category of knowledge is mainly from GaTech OMSCS CSE 6220 Course "Intro to High Perform Computing", including papers, journals, textbooks recommended from the course.

## Syllabus
The course topics are centered on three different ideas or extensions to the usual serial RAM model you encounter in CS 101. Recall that a serial RAM assumes a sequential or serial processor connected to a main memory.

### Unit 1: [[Two-level Mem Model]]
In this model, we return to a serial RAM, but instead of having only a processor connected to a main memory, there is a smaller but faster scratchpad memory in between the two. The algorithmic question here is how to use the scratchpad effectively, in order to minimize costly data transfers from main memory.

Sub-topics include:
- **Basic models** Efficiency metrics, including “emerging” metrics like energy and power 
- **I/O-aware algorithms** Cache-oblivious algorithms

### Unit 2: [[Work-Span Model]]
In this model, the idea is that there are multiple processors connected to the main memory. Since they can all “see” the same memory, the processors can coordinate and communicate via reads and writes to that “shared” memory.

Sub-topics include:
- Intro to the basic algorithmic model, [[Work-Span Intro to OpenMP|Intro to OpenMP]], a practical programming model 
- [[Work-Span Comparison-Based Sorting]], [[Work-Span Scans & List Ranking]]
- [[Work-Span Scans & List Ranking#Scan on Postorder tree|Tree Scan-based computation]], Graph algorithms, e.g., [[Work-Span BFS|Breadth First Search]]
- [[CUDA Parallelism]]

### Unit 3: Distributed memory or network models
In this model, the idea is that there is not one serial RAM, but many serial RAMs connected by a network. In this model, each serial RAM’s memory is private to the other RAMs; consequently, the processors must coordinate and communicate by sending and receiving messages.

Sub-topics include:
-  **[[Dist. Mem - MPI]]** Intro to the Message Passing Interface, a practical programming model 
-  **Reasoning about the effects of [[Dist. Mem - Network Topology]]**, [[Dist. Mem - Dense Matrix Multiply]]
-  **[[Dist. Mem - Sorting]]** Sparse graph algorithms Graph partitioning, [[Dist. Mem - BFS]]