![[OSI model.png]]

##### Application Layer
- service
- interface
- protocols.
	- HTTP (web)
	- SMTP (email)
	- TFP (file transfer)
	- DNS (domain name - IP address translation)

##### Presentation Layer
The presentation layer plays the intermediate role of formatting the information that it receives from the layer below and delivering it to the application layer.

##### Session Layer
 manages the different transport streams that belong to the same session between end-user application processes.

 ##### Transport Layer
 responsible for the end-to-end communication between end hosts.
 protocols:
 - TCP: 
	 - a connection-oriented service to the applications that are running on the layer above, guaranteed delivery of the application-layer messages, flow control which in a nutshell matches the sender’s and receiver’s speed, and a congestion-control mechanism, so that the sender slows its transmission rate when it perceives the network to be congested.
 - UDP: 
	 - a connectionless best-effort service to the applications that are running in the layer above, without reliability, flow or congestion control.

##### Network Layer
deliver the datagram to the transport layer in the destination host
protocols:
- IP
- routing protocols

##### Datalnk layer
responsible to move the frames from one node (host or router) to the next node. protocols:
- Ethernet
- PPP
- WiFi

##### Physical Layer
The physical layer facilitates the interaction with the actual hardware. It is responsible to transfer bits within a frame between two nodes that are connected through a physical link. The protocols in this layer again depend on the link and on the actual transmission medium of the link. One of the main protocols in the data link layer, Ethernet, has different physical layer protocols for twisted-pair copper wire, coaxial cable, and single-mode fiber optics.

## End-to-End principal
Keep core internet structure as simple as possible, more unnecessary features out of the core internet layers and to application layers. 

Some violations
- firewalls and traffic filters. Firewalls usually operate at the periphery of a network and they monitor the network traffic that is going through, and allow or drop traffic, if the traffic is flagged as malicious. Firewalls violate the e2e principle since they are intermediate devices that are operated between two end hosts and they can drop the end hosts communication.
- NAT. It translates WAN and LAN address. 

## Evolutionary Architecture model
![[L1-1 Evolutionary Architecture Model.jpg]]