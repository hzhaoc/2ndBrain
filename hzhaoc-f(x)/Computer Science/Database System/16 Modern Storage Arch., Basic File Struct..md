## **Ch16: Disk Storage, Basic File Structures, Hashing, and Modern Storage Architectures**

_Introduction_

- Primary Storage: main memory (DRAM), cache memory (RAM)
- Secondary Storage: magnetic disks, flash memory (like SSD, USB).
- Tertiary storage: optical disks (CD-ROMs, DVDs), tapes. Larger capacity, lower cost, slower access

_ **Primary File Organizations** _

- Heap file: no order
- Sorted file: ordered
- Hashed file: use a hash function applied to a particular field (hash key) to determine a record&#39;s placement on disk
- Trees

_Secondary file organizations_

- Use alternative fields to access file records like indexes

_Secondary Storage Devices_

![[Secondary Storage Devices1.png]]
![[Secondary Storage Devices2.png]]

_ **Some notes about Disk:** _

- **I/O Latency** :
![[disk_io_latency.png]]
	1. Seek time (time the read/write head moves to the target track)
	2. Rotational delay (time the read/write head moves to the target disk sector)
	3. Transfer time
- **Interface disk drive** to computer system Disk Controller, like SCSI (small computer system interface), SATA (serial attachment)
- **Buffering of data**
- **Proper organization of data** on disk
- Read data ahead of requests
- **Scheduling of I/O requests**
- **Use of log disks** to hold temporary writes
- Use of **SSDs or flash memory** for recovery purposes

_Buffering of Blocks_
- Pin-count
- Dirty bit
- Buffer replacement strategies: LRU, Clock, FIFO

_Placing File Records on Disk_
- Allocating File Blocks on Disk, file segments
- File Header/Descriptor

_Operations on File_
- Open
- Reset
- Find
- Read
- FindNext
- Delete
- Modify
- Insert
- Close
- Scan
- FindAll
- Find
- FindOrdered
- Reorganize