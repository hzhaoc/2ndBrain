This Category of knowledge is mainly from GaTech OMSCS CSE 6220 Course "Intro to High Perform Computing", including papers, journals, textbooks recommended from the course.

## Syllabus
The course topics are centered on three different ideas or extensions to the usual serial RAM model you encounter in CS 101. Recall that a serial RAM assumes a sequential or serial processor connected to a main memory.

### Unit 1: [[Two-level Memory Model]]
In this model, we return to a serial RAM, but instead of having only a processor connected to a main memory, there is a smaller but faster scratchpad memory in between the two. The algorithmic question here is how to use the scratchpad effectively, in order to minimize costly data transfers from main memory.

Sub-topics include:
- **Basic models** Efficiency metrics, including “emerging” metrics like energy and power 
- **I/O-aware algorithms** Cache-oblivious algorithms

### Unit 2: The work-span or dynamic multithreading model
In this model, the idea is that there are multiple processors connected to the main memory. Since they can all “see” the same memory, the processors can coordinate and communicate via reads and writes to that “shared” memory.

Sub-topics include:
- **Intro to the basic algorithmic model** Intro to OpenMP, a practical programming model 
- **Comparison-based sorting algorithms** Scans and linked list algorithms 
- **Tree algorithms** Graph algorithms, e.g., breadth-first search

### Unit 3: Distributed memory or network models
In this model, the idea is that there is not one serial RAM, but many serial RAMs connected by a network. In this model, each serial RAM’s memory is private to the other RAMs; consequently, the processors must coordinate and communicate by sending and receiving messages.

Sub-topics include:
-  **The basic algorithmic model** Intro to the Message Passing Interface, a practical programming model 
-  **Reasoning about the effects of network topology** Dense linear algebra 
-  **Sorting** Sparse graph algorithms ** Graph partitioning