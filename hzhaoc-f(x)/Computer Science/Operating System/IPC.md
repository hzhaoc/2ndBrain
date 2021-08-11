# IPC
Processes interact through IPC (inter-process communication) mechanism. Two ways. 
### Message Passing
![[message passing.png|450]]
Kernel OS creates a buffer/channel and also controls sending or receiving data between two processes.
-  type: pipes, message queues
-  API: sockets

- Pros: Kernel manages IPC. (programmers do system calls to do the data which process communicates what data with which process, and the IPC mechanism is handled by Kernel OS through this shared buffer. _See also [[Multi-Process - Shared Memory#Share Mem vs Message Passing]] for comparison at computer architecture perspective_)
- Cons: Overhead of needs to transfer data between processes in buffer channel, data need to be copied into buffer first and then copied into another process. 
### Shared Memory
![[shared mem2.png|500]]
Kernel OS establishes a shared memory channel directly between two processes. Shared Memory can be in forms of unstructured set of physical addresses or memory mapped files. After that the shared address space between the two processed can be accesses the same way as non-shared addresses and Kernel OS is out of control.
- Pros: OS out of control. Only one system call to set up the shared memory (which is mapping mapping virtual memory between two processes)
- Cons: 
	- No API interface. more error-prone.
	- communication protocol
	- programmer job to manage shared buffer
	- explicit sync
		- Mutex
		- Message queues  (send/recv)
		- semaphores (binary)
##### Requires sync
- Mutex
- Message queues  (send/recv)
- semaphores (binary)

##### API
- Sys V – segment shared memory
- POSIX
- Mapped files
- Android ashmen

##### fun fact
Windows use "local" procedure calls which does message passing if data small, or shared memory method if data large.

##### message buffer vs shared memory
message buffer copy data; shared memory has overhead to map virtual addr to  shared mem

### RPC
- high level interface for cross-machine communication
- hides complexity

##### RPC requirements
![[rpc.png|500]]
1. client/server interactions
2. procedure call interface
3. type checking
	1. error handling
	2. packet bytes interpretation
4. cross-machine conversion
	1. such as big-little endian
5. higher level protocol
	1. access control, fault tolerance
	2. work under different transport protocols, e.g. UDP, TCP

##### RPC example
1. client machine call "Add function" (think of it as a complex computation function that only sever is capable of doing so)
2. function execution jumps to an address space of a stub implementation
3. stub builds message (what is the function, what is input), does RPC
4. message is sent to server across network
5. server OS hands message to sever stub
6. stub unpacks/parse message,
7. stub make local call in the user level OS
8. does actual Add
9. sent result back to client through network
![[rpc example.png|800]]

##### RPC steps
0. register: server "registers" procedure, args types, location...
1. bind: client finds and  "binds" to server
2. call: client makes RPC call; control passed to client stub, client code blocks
3. marshal: client stub "marshals" arguments (serialize  args into buffer)
4. send: client sends message to sever
5. receive: server receives message; pass msg to server-stub; access ctrl checks
6. unmarshal: sever stub unmarshal args (extracts args &  create data structs)
7. actual call: server performs operation and computes result of RPC operation
8. return: server return result to client in a reverse path