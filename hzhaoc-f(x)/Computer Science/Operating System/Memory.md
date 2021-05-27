# Concepts
-  allocate
	-  allocate physical memory, replacement contents in physical memory with disks
-  Arbitrate
	- translate virtual address to physical address, validate
# Hardware support of MM
- MMU
	- (memory management unit): translate virtual to physical addr, or report faults (illegal, permission, not present), by page table/segments
- Registers
	- pointers to page table or base, limit size, number of segments
- Cache
	- (**TLB**) translation lookaside buffer, part of virtual-physical translations (faster than page table/segments)
- Translation
	- hardware actually performs translation.
- Copy-on-write (‘COW’)
	- when creating a new process from copying an original process, new process pointer points to original page (static portion, write-protected). When a write request issued, copy only the part that will be written (updated part)
	- Copy-on-write (COW), sometimes referred to as implicit sharing or shadowing. **the copy operation is deferred until the first write**. By sharing resources in this way, it is possible to significantly reduce the resource consumption of unmodified copies, while adding a small overhead to resource-modifying operations.
- Checkpointing
- Debugging, migration (same mechanism as checkpointing)
# Type
## Page-based
- Allocate
	- fixed-size page in virtual memory -> page frames in physical memory
- Arbitrate
	- page tables
### Page tables
- Virtual memory pages and physical memory page frames are the **same size**.
- VPN (Virtual Page Number / first address in virtual page) is the index/offset in the page table, it directs to the PFN (page frame number, first addr in physical page frame) through page table. Offsets followed by VPN are also passed to offsets followed by PFN, resulting in a complete virtual to physical data mapping through page table. Page table also has a valid bit field, indicating mapping is valid or invalid (return fault). When a reclaimed page/data goes back to DRAM/physical mem from disk, new mapping is built. Physical address may be different from before.
- When a variable is declared, a virtual memory address is allocated. When it’s initialized, OS first time touch the corresponding physical address
- ![[page_table.png]]
- In context switch, page table is switched by changing a register pointer. e.g. CR3 on x86
- Page table has many entries other than valid bit, PFN
- Multilevel Page Table:
	- Pros: smaller internal page tables
	- Cons: increase translation latency
- Page table cache (TLB) e.g. x86 Core I7: per core: 64-entry data TLB, 1280-entry instruction TLB, 512-entry shared second level TLB
- Inverted Page Tables, index is PFN, fields are process ID and VPN, needs to search
- Hashing Page Table. VPN -> hash function -> hash table entry/index -> list of possible PFN
- Larger page sizes
	- Pros: fewer page table VPN/entries, smaller page table size, more TLB hits,
	- Cons: internal fragmentation (wasted memory gaps)
### Demand paging
Virtual memory >> physical memory
Swap virtual memory in/out of disks <-> memory
When a virtual page is not present in memory and it’s referenced:
![[demand_paging.png]]
1. Instructions execute ‘reference’ to that page in page table
2. Page table finds **Present Bit** of that VPN is 0 -> return page fault error, cause trap in OS
3. Kernel OS takes control, sees page fault error, finds page in backing store
4. Kernel OS issues I/O operation, bringing back missing page
5. OS determines a free physical page frame for that missing virtual page, update corresponding VPN in page table
6. OS restarts instructions, program counter points to ‘reference’ in 1 again. User kernel takes control. Re-execute ‘reference’.
If a page is “pinned”, swapping disk <-> memory is disabled, useful for DMA
### Page swap
- LRU policy / access bit to track page usage
- Dirty bit to track page modification
- Avoid non-swappable pages

## Segment-based
- Allocate: flexible-size segments in virtual memory -> some regions in physical memory and swap in/out of disks
- Arbitrate: segment registers
- Can be combined with paging to translate virtual to physical addr

## Memory allocation
Memory allocator
###  Kernel level allocator
- Addressing aggregation issues of page allocation
	- Buddy allocator
	Avoids external fragmentation (non-aggregated spaces)
	- ![[buddy_allocator.png]]
	- Slab allocator
	Avoids internal  and external fragmentation
	Caches for common object types/sizes, on top of contiguous memory.
	-  ![[slab_allocator.png]]
	-  Kernel state
	-  Static process state
-  User level allocator
	-  Dynamic process state (**heap**). malloc/free