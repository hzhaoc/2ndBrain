Understanding how to detect and recover from failures of memory & storage is the topic of this lesson. RAID 0 - RAID 6 are discussed.

- fault - module deviates from specified behavior
- error - actual behavior differs from expected behavior, activated fault
- failure - system deviates from specified behavior, resulting error

- Reliability = a measure of the continuous service accomplishment
	- Mean Time To Failure (MTTF) = how long will the system provide service before the next service interruption.
- Availability measures service accomplishment as a fraction of overall time
	- Availability = MTTF/ (MTTF + MTTR)  (MTTR: mean time to repair)


### Improving Reliability and Availability
##### Fault Avoidance
prevent faults from occurring.
##### Fault Tolerance
prevent **faults** from becoming **failures**. For example, ECC (error correction code).
##### Speed up repair for availability

### Fault Tolerance Approach
##### checkpointing
save checkpoints periodically and restore to correct state when error is detected. if restoration takes too long, consider this an interruption. works well for intermittent or transient fault.
##### N-Module Redundancy
- N=2 Dual Module Redundancy - detects but does not correct 1 faulty module
- N=3 Triple Module Redundancy - corrects 1 faulty module 
- N=5 Five Module Redundancy - detects and corrects up to 2 modules
- ...

##### fault tolerance for mem &  storage
- parity: add one extra bit as XOR of the data bits. if it is in error, the parity bit gets flipped.
- ECC: correct single bit, detect two bit errors.
- **RAID**: redundant array of independent disks

### RAID
Redundant Array of Independent Disks
- several disks are used in place of one disk
- each disks detects errors using ECC

Goal of RAID
- better performance
- Read/Write accomplishment even when there is a bad sector or when a disk fails.

##### RAID0
Uses striping to improve performance. RAID 0 takes 2 disks and makes it look like 1 disk. 
- Pros:
	- Twice the data throughput of a single disk
	- Less queuing delay
- Cons:
	- Reliability is worse
- reliability
	-	f = failure rate for a single disk. For a single disk MTTF = 1/f. For N Disks in RAID 0, $MTTF = \frac{1}{N*f}$

##### RAID1 
A second disk is a copy of the first disk. The write performance is the same as for 1 disk. The read performance is twice the performance of one disk. Tolerates any faults that affects 1 disk.
- reliability
	- $MTTDL = (MTTF / 2) + MTTF$
		- MTTDL: mean time to data loss
- Reliability if Disks are Replaced
	- $MTTDL = (MTTF/ 2) * (MTTF/ MTTR)$
		- approx when $MTTR  << MTTF$

##### RAID4
(not often used). The disks are block interleaved. 
For N disks:
- N-1 disks contain striped data like RAID0
- 1 disk has parity blocks (XOR bits in same position in the other N-1 disks)

A damaged disk that cannot be corrected with ECC can be reconstructed by using the parity bit and the data values in the other disks.

RAID4 is a more general technique that mirroring. A write to a RAID4 must write to the required disk and to the parity disk. A read just reads the required disk

- Performance and Reliability
	- read: N-1 of one disk
	- write: 1/2 of one disk (bottleneck is 1 read of old parity disk + 1 write to new parity disk)
	- ![[RAID4 write.png|500]]
	- MTTF
			- (no repair): MTTF/N x MTTF/(N-1)
			- (repair): MTTF/N x MTTF/((N-1) x MTTR)
	
##### RAID5
Distributed block-interleaved parity. The parity is spread throughout all the disks, there is no dedicated parity disk.
![[RAID5.png|500]]

- Read Performance = N * Throughput of one disk
- Write Performance = N/4 * Throughput of 1 disk
- reliability: same as RAID4

##### RAID6
similar to RAID5, with two parity bits per data bit. can work with 2 failed stripes.

- when 1 disk fails, use real parity bit to reconstruct
- when 2 disk  fails, solve some equation to reconstruct.

- RAID6 vs RAID5
	- 2x overhead of parity bits,  more write overhead (6/write vs 4/write)
	- allow one more disk fails. RAID can be only useful when MTTR is long or related fails. usually this is not the case and overhead outweighs benefits of allowing 2 disk failures. So this is often an **Overkill**!