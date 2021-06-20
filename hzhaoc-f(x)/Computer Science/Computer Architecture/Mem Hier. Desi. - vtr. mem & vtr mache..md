> A virtual machine is taken to be an efficient, isolated duplicate of the real machine. We explain these notions through the idea of a virtual machine monitor... A VMM has three essential characteristics. First, the VMM provides an environment for programs which is essentially identical with the original machine; second, programs run in this environment show at worst only minor decreases in speed; at last, the VMM is in complete control of system resources.
> - Gerald Popek and Robert Goldberg

Virtual mem moves pages between levels of mem hierarchy, just as caches move blocks between levels. Likewise, TLBs act as caches on the page table, eliminating the need to do a mem access every time an address is translated. Virtual mem also provides separation between processes that share one physical address but have separate virtual address spaces. 

Virtual machines are foundational technology to cloud computing.

## Protection via Virtual Mem
Page-based virtual mem, including TLB that caches table entries, is the primary mechanism that protects processes from each other. [[Computer Architecture]] & [[Operating System]] join forces to allow processes to share hardware yet not interfere with each other. At minimum, architecture must do the following:
- provides at least two modes: user-level and kernel level processes
- provide a portion of the processor state that a user process can use but not write. 
- provide mechanisms whereby the processor can go from user  mode to supervisor mode and vice versa. The first direction is typically done by a **system call**.
- provide mechanisms to limit mem accesses to protect mem state of a process without having to swap the process to disk on a context switch.

By far the most popular mem protection schemes is adding protection restrictions to each page of virtual memory. For example, in a [[Mem Mgmt#Page table|page table]] that translates virtual addr to physical addr, each page entry contains additional bits includes information that whether a user process can read this entry, write this entry, and whether code can be executed from this page entry. Only OS can update the page table.

TLB uses principal of locality which states that if mem accesses have locality, then the addr translations for the accesses must also have locality. By keeping these addr translations in a special cache (TLB), a memory access rarely requires a second access to translate the addr. A TLB entry is like a cache entry where tag holds portions of the virtual addr, and data portion holds a physical page addr, protection bit, valid bit, use bit, dirty bit.. OS change these bits by changing the value in the page table and then invalidating the corresponding TLB entry. When the entry is reloaded from [[Mem Mgmt#Page table|page table]], TLB gets accurate copy of the bits.

Current production Operating Systems have thousands of bugs. This stimulates a protection model with a much smaller OS code base than full OS, such as virtual machines.

## Protection via Virtual Machine
We are interested in VMs that provide a complete system-level environment at the binary ISA level. When the [[Inst Set Arch.#Instruction Set Architecture|ISA]] presented by VM and the underlying hardware match, such VMs are called _(operating) system virtual machines_. With VMs, multiple OSes share the hardware resources. 

The software that supports VMs is called a _virtual machine monitor_ or _hypervisor_; the VMM is the heart of the virtual machine technology. The underlying platform is called the _host_, and its resources are shared among _guest VMs_. The VMM determines how to map virtual resources to physical resources:  A physical resource may be time-shared, partitioned, or even emulated in software. The VMM is **much smaller** than a traditional full OS; the isolation portion of a VMM is perhaps only 10,000 lines of code. 

The cost of **processor virtualization** depends on the workload. User-level processor-bound programs have zero virtualization overhead because the OS is rarely invoked, so everything runs at native speeds. Conversely, I/O intensive workloads generally are also OS-intensive and execute many system calls (doing I/O  operations) and privileged  instructions that can result in high virtualization overhead. The overhead is determined by number of insts that must be emulated by the VMM and how slowly they are emulated. On the other hand, cost of I/O-intensive processor virtualization can be hidden by low processor utilization because it is often waiting for I/O.

Although designers' interests in VMs are improving process protection. VMs also provide below commercial benefits:
1. Managing software. VMs provide an abstraction that can run the complete software stack.
2. Managing hardware. 
	1. have each applications run on its compatible version of OS while sharing hardware through VMs.
	2. VMMs support migration of a running VM to a different computer, either to balance load or to evacuate from failing hardware.

## Requirement of a VMM
Qualitative requirements:
- Guest software should behave on a VM exactly as if it were running on the native hardware, except for performance-related behavior or limitations of fixed  resources shared by multiple VMs.
- Guest software should not be able to directly change allocation of real system resources.

To be in charge, the VMM must be at a higher privilege level than guest VMs, which generally runs in user mode; execution of any privileged instructions will be handled by the VMM. The basic requirements of system virtual machines:
- at least two processor modes: system & user
- a privileged subset of insts that is available only in the system mode, resulting in a **trap** if executed in user mode where kernel/system OS take over. All system resources must be controlled only by these privileged insts.

## [[Inst Set Arch.#Instruction Set Architecture|ISA]] support for Virtual Machines
An architecture that allows the VM to execute directly on the hardware is called **virtualizable**, such as IBM 370. RISC-V has support for virtualizations. As said above, when guest VM tries to execute privileged insts, it traps and VMM intercept it and support a virtual version of such information as the guest OS expects.

## Impact of Virtual Machines on Virtual Mem & I/O
Another challenge is virtualization of virtual mem, as each guest OS in every VM manages its own page tables. To make this work, guest VM translates virtual mem to real mem (intermediary add managed by VMM), then VMM translates real mem into physical mem (on hardware).

Another way is for the VMM maintains a _shadow page table_ that maps directly from the guest virtual address to physical hardware address. VMM traps any attempt by guest OS to change its page table or to access page table pointer.

To virtualize the [[Mem Mgmt#TLB|TLB]] in many RISC computers, the VMM manages the real TLB and has a copy of the contents of the TLB of each guest VM. Any inst  that access that TLB must trap. TLB with process ID tags can support a mix of entries from different VMs and VMM, thereby avoiding TLB flush of the TLB on a VM switch. Meanwhile VMM supports a mapping between VMs' virtual process IDs and the real Process IDs. 

Final part is to virtualize I/O. This is by far the most difficult one due to increasing number of I/O devices. The VM illusion can be maintained by giving each VM generic versions of each type of I/O device driver, and then leaving it to the VMM to handle real I/O.

## Extending Inst Set for efficient virtualization & better security
Professor designers including AMD and Intel have introduced this extensions to more efficient virtualizations. Two main areas focus on page tables, TLBs & I/O. IBM implemented _nested page table mechanism_ rather than a single set of shadow page tables to avoid unnecessary TLB flushes. To improve I/O performances, architectural extensions are added that allow a device to directly use DMA to move data and allow device interrupts and commands to be handled by the guest directly.

More recently, Intel introduced a set of extensions to allow user programs to create _enclaves_, portions of code and data that are always encrypted and decrypted  only on use and only with the key provided by the user code. This protects VM applications from Trojan horse user program which typically exploits an OS flaw where user takes control of OS or gain privileged mode to attack.

## Cross-Cutting issues
IBM is still the gold standard of virtual machine technology as of 2017! 
#### Autonomous Inst Fetch Units
Many processors with out-of-order execution and even some with simply deep pipelines decouple the instruction fetch and sometimes initial decode, using a separate inst fetch unit. Typically inst fetch unit accesses the **inst cache** to fetch an entire block before decoding it into individual insts. In addition, the inst fetch unit may prefetch blocks into L1 cache. This reduce total miss penalty. Many processors also include data prefetching, which may increase data cache miss rate, while decreasing miss penalty.
#### Speculation and Mem Access
One major advanced pipeline technique is speculation, whereby an inst is tentatively executed before the processor knows whether it is really needed. Such technique relies on [[ILP - Ctrl Deps. Branch Predict|Branch Prediction]] which if incorrect, the speculated instructions are flushed. There are two main issues with speculation:
1. Protection. Correctly speculated insts may generate exception of protection.
2. Because a speculative processor may generate accesses to both inst and data caches and not use results of those accesses, cache miss rates may raise.
#### Special Inst Caches
One of the biggest challenge in superscalar processors is to supply sufficient inst bandwidth. For designs that translate insts into micro-operations such as most recent Arm and i7 processors as of 2017, inst bandwidth demands and branch misprediction penalties can be reduced by **keeping a small cache of recently translated insts**.
#### Coherency of Cached Data
Multiple processors and I/O devices raise the issues for copies among different levels of mem/caches to be inconsistent. A program running on multiple processors may want to have copies of same data in several caches. The question for I/O is this: where does I/O occur - between I/O and cache or between I/O and mem. To prevent I/O system from interfering with cache as little as possible and still avoid stale data problem, many systems prefer I/O occurs directly to main mem, with main mem acting as  an I/O buffer. Processor cache coherency will be discussed in details in [[TLP]]