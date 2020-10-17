## Description

处理器一般指重要处理器CPU，现在的（2020）的CPU是一个大规模[[Computer Hardware|集成电路]]，是计算机的运算核心和控制核心。功能主要是解释计算机指令和处理计算机软件数据。

大多数现代电路设计用信号线上的高电压和低电压表示不同位值。要实现一个数字系统需要是哪个主要组成部分：
-	计算单元：计算对位进行操作的函数的组合逻辑（ALU）；
根据事先编好的程序，一次从存储器中取出各条指令，放在指令寄存器（[[Computer Hardware|Instruction Register]]）中，通过指令译码分析（Instruction Decoder）确定应该进行什么操作，然后通过操作控制器（Operation Controller）
-	存储单元：存储为的存储器元素（寄存器）；
-	控制单元：控制存储器云阿苏更新的时钟信号；

## Power
Power consumption of each core is modeled as two major parts: active power due to [[Computer Hardware|transistor]] switching and static power due to leakage.\
$$P_{total}=P_{active}+P_{leakage}$$

### Active Power
$$P=\frac{1}{2}C*V^2*f*\alpha$$
where
$C$ is [[Electricity|Capacitance]] (~chip area).
$V$ is [[Electricity|Voltage]].
$f$ is **clock frequency**. It measures number of cycles CPU executes per second, measured in GHz. A cycle is a pulse synchronized by an [[Computer Hardware|Crystal Oscillator]], a helper to measure running speed of CPU. During each cycle, billions of transistors open and close. Multiple instructions may be completed in one cycle or multiple cycles.
$\alpha$ is activity factor.

### Static Power
The lower voltage, the higher leakage.
![[CPU-power.png]]

