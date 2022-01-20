Transport layer on the sending host receives message from application layer and appends its own header as a **segment**, which is then sent to network layer which will append this segment with its header information. Then it will send it to the receiving host via routers, bridges, switches, etc.

> Why transport layer between network layer and application layer? **TCP guarantees in-order delivery of the application-layer data without any loss or corruption.**

Transport layer does multiplexing by ports. There are two ways we can use multiplexing: Connectionless and connection-oriented multiplexing. As the name suggests, it depends if we have a connection established between the sender and the receiver or not.

Why do we have UDP in the first place? As it turns out, it is exactly the lack of those mechanisms that make UDP more desirable in some cases.

Specifically, UDP offers fewer delays and better control over sending data because with UDP we have the following:

1.  **No congestion control or similar mechanisms.** As soon as the application passes data to the transport layer, UDP encapsulates it and sends it over to the network layer. In contrast, TCP “intervenes” with a congestion-control mechanism or retransmission of unacknowledged packets. These TCP mechanisms cause further delays. 
2.  **No connection management overhead.** We will see that TCP uses a three-way handshake before it begins transferring data. UDP forgoes the connection and starts sending data immediately. The lack of connection establishment and maintenance means even fewer delays will occur.

![[tcp 3way handshake.png]]