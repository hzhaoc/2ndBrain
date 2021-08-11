# Trends in Power and Energy in Integrated Circuits
## Systematic perspective
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

## Dynamic & Static
Power consumption of each core is modeled as two major parts: active power due to [[Computer Hardware|transistor]] switching and static power due to leakage.\
$$P_{total}=P_{active}+P_{leakage}$$

### Active Power
$$P=\frac{1}{2}C*V^2*f*\alpha$$
where
- $C$ is [[Capacitance]] (~chip area).
- $V$ is [[Electromagnetism|Voltage]].
- $f$ is **clock frequency**. It measures number of cycles CPU executes per second, measured in GHz. A cycle is a pulse synchronized by an [[Computer Hardware|Crystal Oscillator]], a helper to measure running speed of CPU. During each cycle, billions of transistors open and close. Multiple instructions may be completed in one cycle or multiple cycles.
- $\alpha$ is activity factor.

### Static power
- As voltage goes lower, dynamic power goes down, and static power goes up due to leakage. There's a minimum power solution where voltage is either not too high or too low.
- **Static power** is proportional to **static current** times **voltage**. 
- This static power leakage is increasing. The only hope is to turn off power to the chip's subsets.
- the lower voltage, the higher leakage.
![[CPU-power.png]]
- Finally because processor power is just part of the whole system, it can make sense to use a faster, less energy-efficient processor to allow rest of system to go into sleep mode, *race-to-halt*.