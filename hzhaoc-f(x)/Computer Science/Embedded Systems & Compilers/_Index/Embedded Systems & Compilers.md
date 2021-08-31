this entry knowledge is mainly from OMSCS CS 6291 Fall 2021, including papers and textbooks recommended. 
-  textbooks:
	-  Embedded Computing: A VLIW Approach to Architecture, Compilers and Tools
	-  Compilers: Principles, Techniques, and Tools

# Note List
- [[VLIW Compiler]]
- [[Embedded Processor Market]]

# Some Background
### [[Bg, Trend, Cost, Power, Energy, Perform#Intro|RISC]] vs CISC
![[RISC vs CISC.png|600]]
- RISC
	- lower per chip cost
	- require more instructions to do the same thing the CISC program does.
	- code expansion can be a problem
- CISC
	- reducing the gap between programming and hardware
	- makes more efficient use of a slow memory (many insts can access memory; in RISC there're only loads/stores)
	- instructions take different amounts of time to execute (variable length insts)

example of RISC vs CISC on same program:
- RISC:
```code
load r5 <- 4[r1]
add r5 <- r5 + r2
store 4[r1] <- r5
```
- CISC
```code
add 4[r1] <- r2
```
