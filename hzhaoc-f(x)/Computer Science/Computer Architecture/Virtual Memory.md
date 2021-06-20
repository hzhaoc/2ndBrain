This lesson discusses the difference between virtual and physical memory. Virtual memory isused by programs and must be translated to physical memory. Since the translation can beslow, a Translation Look-Aside-Buffer (TLB) is used.

##### why virtual mem?
- Hardware view of memory:
the memory is a block of memory with a specific address allocated to each location.

- Programmer’s View of memory:
memory is large arrays with many more addresses than the actual memory. Each program has its own view of the memory.

Virtual memory reconciles the programmer’s view of memory with the hardware memory

##### processor view of mem
The processor sees the physical memory (actual memory). The actual amount of memory is sometimes < 4 GB. Although the address space is 64 bits, there is never this much memory (16 Exabytes/process). **There is a 1:1 mapping of bytes to words** (1 virtual addr to 1 phys addr & 1 phys addr to 1 virtual addr)

##### program view of mem
Programs sees the **stack & heap**, with a large gap between the two. **The gap is never fully used.** So the programs see much more memory than the actual memory, so virtual memory is used.

### V <-> P 
- physical memory is divided into 4k Byte frames
- virtual memory is divided into 4k Byte pages. 
- operating system uses page tables to map the pages to frames. If programs use the same physical memories, then the pages are mapped to the same frame.

##### where does mem gap between virtual and physical go?
virtual mem usually > phys mem. the difference is stored in **disk**

##### V->P translation
1.  **virtual addr = page # + offset**. 
2. **page # maps to frame #**
3. **frame # + same offset = phys addr**
- overview: virtual mem is divided into pages. a page # + offset maps into a frame # + offset as phys addr through a page table.
![[virtual to phys mem.png|600]]

### Page Table
suggested another reading of [[Mem Mgmt#Page table|page table]] under operating system.
##### flat page table
- size
page table size = (vtr mem size / page size) * page table entry size (to store frame #)

some of these pages in vtr mem are never accessed. like the ones between **heap & stack**. so a flat page table is unnecessarily large per process. 

##### multi-level page table
- Multi-level page tables are used for large virtual memories.
- Multi-level page tables avoid having page entries for the unused virtual memory addresses
- **most outer-pages in outer page table will be unused and its corresponding inner page tables will be eliminated, thus saving space.**
![[multi-level page tables.png|600]]

##### choose a page size
the larger a page is, the smaller the page table is for translation (pro), the more likely **internal fragmentation** will result (con). a good compromise is usually a size **from several KB to several MB**. 

### access time with V->P translation
see below picture, a typical load/store instruction does follow cycles:
1. compute vtr addr (quick)
2. compute page # (quick)
3. translation process
	1. compute phys addr of page table entry (page table start addr + page #) (quick)
	2. read that page table entry **(slowest! may need access to memory because page table is not guaranteed to be small enough to be in cache or cpu!)**
	3. compute phys addr (loaded frame # + offset) (quick)
4. access cache (if miss, continue access mem which is slow)

As you can see, **if page tables are stored in memory, (or even in regular cache), a load/store access does many cycles!**
![[access time for V-P translation.png|700]]

### TLB
To speed up the translation, a special, small cache is used, called the TLB (**translation lookaside buffer**).

TLB directly maps **from vtr page # to frame #** for physical addr access no matter how many levels of page tables there are. It is small. so very fast.

##### TLB Miss
- software TLB miss handling
fancy, [[Operating System]] does the job of put translations into TLB. so OS can design any forms of page tables: tree, hash table...

- hardware TLB miss handling
processor does TLB update automatically. faster. needs hardware support. 
because hardware is cheap (2021), most uses hardware TLB miss handling. some embedded processors use software approach due to low frequency of TLB miss or cost of Hardware TLB handling support.

##### TLB structure
TLB is a specific cache. structure is similar to regular cache.
- assoc?
TLB already fast. so do highly-associative set cache like TLB.

- size?
want to cover cache data blocks. usually 64-612 entries.

- need more?
	-	multi-level TLB. (e.g. 2-level TLB: L1 small & fast; L2 hit time several cycles & large but still a lot faster than mem.)
		-	**when TLB miss on one level, consult next level, until highest level is reached and still miss, do page table translation and update it into all levels consulted.**