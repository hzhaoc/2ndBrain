Predication avoids predicts. It simply do work on both sides: not taken inst and taken inst. This way it always throw away work from the wrong path, thus always wast up to 50% work.

- for deep `LOOP`,`RET`,`FUN`, large `IF-ELSE-THEN`, use prediction; 
- for small `IF-ELSE-THEN`, use predication.

## if-else conversion to predication insts
- Conditional move. 
	-	MIPS: `MOVZ x1, x2, COND`（if COND==0, Move x1 to x2）, `MOVN x1, x2, COND` (if COND!=0, move x1 to x2)
	-	x86: `CMOVZ`, `CMOVNZ`, `CMOVGT`
	-	Note that conditional instructions require compiler support to convert if-else to predication insts. typically more registers are needed and more insts are executed compared to small if-else insts. it typically removes hard-to-predict branches. More [[Storage Hierarchy#Register|Register]] and more instructions need **extensive hardware support** to achieve full predication.

## full predication
every inst has a conditional bit
-	ITANIUM: support condition bit on EVERY instruction
```
MPEQZ p1, p2, R1
(p2) ADD1 R2, R2, 1
(p1) ADD1 R3, R3, 1
```
`MPEQZ` is predication equal zero conditional move so if R1 == 0, p1 = 1, p2 = 0, else p1 = 0, p2 = 1. then (p2), (p1) are qualifying predication to do ADD1 or not.