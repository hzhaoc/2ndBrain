#  Intro
Assembly language programming elimination and standardized vendor-independent operating systems creation such as UNIX bring out a new set of architecture with simpler instructions called RISC (Reduced Instruction Set Computer). RISC-based machines focused on two performance techniques: 
- instruction level parallelism ([[ILP - ILP & Deps.]], initially pipelining)
- cache optimization

RISC-based computers outcompeted peers. Intel rose to challenge primarily by translating 80x86 instructions into RISC-like instructions internally. As transistor counts soared in 1990s, hardware overhead of translating the more complex x86 architecture became negligible. In low-end applications such as cell phones, this overhead led to a RISC architecture,  **ARM**, becoming dominant.

In 1974,  Robert Dennard observed **Dennard scaling**: power density was constant for a given area of silicon even with increased number of transistor because of smaller dimensions of each. Transistors could go faster but use less power. Dennard scaling ended around 2004 because current and voltage couldn't keep dropping and still maintain dependability of integrated circuits. This change **forced** processor industry to use multiple efficient processors or cores instead of uniprocessor. This switch is not optional at the time. It indicates architect focus transitioning from solely relying on ILP to data-level parallelism (DLP), thread-level parallelism (TLP), request-level parallelism (RLP) among WSCs (warehouse-scale computers). Whereas compiler and hardware conspire to exploit ILP implicitly without programmer's attention, DLP,  TLP, RLP are explicitly parallel, requiring restructuring of applications for such types of parallelism, a new burden for programmers.

Second observation is **Moore's Law** which is number of transistors per chip would double every two years. It ended somewhere around 2010.

The ending of Moore's Law, Dennard Scaling, unchanging power budgets for microprocessors, replacement of power-hungry uniprocessor with energy-efficient multiprocessors, limits to multiprocessing to achieve **Amdahl's Law**,  together cause improvement in processor performance to slow down. And the only path left to improve **energy-performance-cost** is **specialization** - **domain-specific cores or processors.**

### Classes of Computers
- Internet of Things (IoT) / [[Embedded Systems & Compilers|Embedded Computer]]
- Personal mobile device
- Desktop/Laptop Computing
- Server
	- Availability
	- Scalability
	- throughput
- Clusters / WSCs
	- A collection of **desktop computers or servers** connected by local area networks to act as a single larger computer. Each node running its own operating system, and nodes communicate using a networking protocol.
	- Focus on performance and power.
	- Difference between WSC and server is WSCs use redundant inexpensive components as building blocks, relying on software layer to catch and isolate many failures in computing to deliver availability needed for such applications. Scalability is handled by networking protocol instead of integrated computer hardware as in the case of servers. 

### Classes of Parallelism
##### Application level
- DLP
data-level parallelism arises because there are many data items that can be operated at the same time.

- TLP
Task level parallelism arises because tasks of work are created that can operate independently and largely in parallel.

##### Hardware level
to implement application level parallelism, hardware can in turn exploit in four ways:
- ILP
_instruction-level parallelism_ exploits _data-level parallelism_ at modest levels with compiler help using ideas like **pipelining** and at medium levels using ideas like **speculative execution**.

- Vector architecture, GPUs, multiple instruction sets
applying a single instruction to a collection of data in parallel.

- TLP
thread-level parallelism exploits either data-level or task-level parallelism in a tightly coupled hardware model that allows for interaction between parallel threads.

- RLP
request-level parallelism exploits parallelism among largely decoupled tasks specified by the programmer or the operating system.

### Define Computer Architecture
- ##### [[Instruction Set Arch.#Instruction Set Architecture|ISA]]: myopic view of computer architecture
- ##### Genuine computer architecture
software function needs demand computer architecture

### Trends in Technology
- *Integrated circuit logic technology* — Moore's Law ended.
- *Semiconductor DRAM* — seemingly no 32-GB DRAM.
- *Semiconductor Flash* — electronically erasable programmable read-only memory. Standard storage device in PMDs. SSD is rapidly increasing and replacing magnetic disk. A lot cheaper than DRAM.
- *Magnetic disk technology* — a lot cheaper than flash memory. Central to server and WSCs.

##### Scaling of transistor and wires
To a first approximation, in the past, the transistor size decrease linearly or **count increase quadratically** with **linearly increase in overall performance**. And wires do not. **Wire delay** is a design obstacle for large integrated circuits. **Larger and larger fractions of clock cycle have been consumed by propagation delay of signals on wires, but power now plays an even greater role than wire delay**. 

### Fallacies & Pitfalls
- all exponential laws must come to an end
- multiprocessors trend is because there's no other option
- redundant system components to avoid single point of failure (fault-tolerant)
- benchmarks don't remain valid indefinitely
- disks never fail

# Trends in Cost, Power, Energy, Performance
- Quantitative Principles of Computer Design
	- parallelism
	- locality
	- common use priority
	- Amdahl's Law

### Cost
- *learning-curve* drives down manufacturing cost by time even without technology improvement. Technology iteration.
- If demand & supply are balanced, and there's sufficient market competition, price & cost track closely.
- economic scaling.
- commodity business in PC compete and gain manufacturing efficiency with scaling at very limited profit. 
- DRAM, SSD, monitors, etc are pretty standardized and thus commoditized; processors vary. Thus integrated circuits cost are important among peers for computers.

##### Cost of an [[Integrated Circuit]]
basic process of silicon manufacture is unchanged: a wafer is tested and chopped into dies that are packaged. Cost of an packaged IC is:
- $$Cost\ of \ IR \ = \ \frac{Cost\ of\ die \ + \ Cost \ of \ testing \ die \ + \ Cost \ of \ packaging \ and \ final \ test }{final \ test \ yield}$$

- $$Cost \ of \ die = \ \frac{cost \ of \ wafer}{dies \ per \ wafer \ X \ die \ yield}$$

- $$dies \ per \ wafer \ = \ \frac{\pi*(wafer \ diameter/2)^2}{die \ area}-\frac{\pi * wafer \ diameter}{\sqrt{x*die \ area}}$$

In the third formula, first term is ratio of wafer area to die area, second compensates for "square peg in a round hole" approximately.

- $$Die \ yield \ = \ wafer \ yeild \ * 1/(1+\ defects \ per \ unit \ area * die \ area)^N$$

This is Bose-Einstein empirical model. N is a manufacturing process complexity. 

##### just some facts
- DRAMs include redundant memory cells for fault-tolerant -> higher manufacturing yield, lower cost.
- TSMC 2020 300mm wafer at 5nm at ~ $17K cost.
- I/O pins plus functions determine die size.
- testing add prior cost by 50%!
- for low volume IR manufacturing, [[Photomask]] can be a non-negligible cost.

### Trends in Power and Energy in Integrated Circuits
##### Systematic perspective
- air-cooling limit is usually at around 100W.
- Maximum power?
- long-term average power? TDP (thermal design power). Heat management:
	- lower clock rate
	- if the first one not good, thermal overload trap.
- Energy efficiency. Energy efficiency is **energy consumption for a given task**. To improve energy consumed for a given task. Ways to improve:
	- turn off inactive module
	- Dynamic voltage-frequency scaling DVFS. lower freq for low activities. 
	- Design for typical case. lower freq for idled DRAM & Disk spins.
	- Overclocking

##### Dynamic & Static
Power consumption of each core is modeled as two major parts: active power due to [[Computer Hardware|transistor]] switching and static power due to leakage.\
$$P_{total}=P_{active}+P_{leakage}$$

##### Active Power
$$P=\frac{1}{2}C*V^2*f*\alpha$$
where
- $C$ is [[Capacitance]] (~chip area).
- $V$ is [[Electromagnetism|Voltage]].
- $f$ is **clock frequency**. It measures number of cycles CPU executes per second, measured in GHz. A cycle is a pulse synchronized by an [[Computer Hardware|Crystal Oscillator]], a helper to measure running speed of CPU. During each cycle, billions of transistors open and close. Multiple instructions may be completed in one cycle or multiple cycles.
- $\alpha$ is activity factor.

Usually $V$ and $f$ are kept to change proportionally to keep circuit reliable, mainly due to reliability in the presence of environmental noise.

##### Static power
- As voltage goes lower, dynamic power goes down, and static power goes up due to leakage. There's a minimum power solution where voltage is either not too high or too low.
- **Static power** is proportional to **static current** times **voltage**. 
- This static power leakage is increasing. The only hope is to turn off power to the chip's subsets.
- the lower voltage, the higher leakage.
![[CPU-power.png]]
- Finally because processor power is just part of the whole system, it can make sense to use a faster, less energy-efficient processor to allow rest of system to go into sleep mode, *race-to-halt*.

Perspectives to think about computer architecture:
-	Performance
-	Energy efficiency
-	Cost

Only consistent and reliable measure of performance is** execution time of real programs**.

### Performance
##### Common Metrics
-	Latency (start -> done)
-	Throughput (# / second )
-	$Speedup_{x:y}$ = $\frac{latency_y}{latency_x}$ =$\frac{throughput_x}{throughput_y}$ 

##### Benchmark
- Standard
	- SPEC
	- ...
- Benchmark performance metrics
	- (geometric) Average execution time
	- $$CPU \ time \ = \ \sum{(\frac{instructions}{program} * \frac{cycles}{instruction})} * \frac{time}{cycle}$$
		-	insts #:	algorithm, compiler, **instruction set**;
		-	CPI:	**instruction set**, **processor design**;
		-	clock freq:   **processor design**, circuit design, transistor physics.

##### Amdahl's Law:
$$Overall \  Speedup = \frac{1}{(1- P) + \frac{P}{S}}$$
where
$P$ is part of the program execution **time** (not instructions) that is enhanced
$S$ the speedup for that part