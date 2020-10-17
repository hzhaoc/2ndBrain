Predication avoids predicts. It simply do work on both sides: not taken inst and taken inst. This way it always throw away work from the wrong path, thus always wast up to 50% work.

For deep `LOOP`,`RET`,`FUN`, large `IF-ELSE-THEN`, use prediction; 
for small `IF-ELSE-THEN`, use predication.

## Simplest predication
Conditional move. 
-	MIPS: `MOVZ x1, x2, COND` （if 0）, `MOVN x1, x2, COND` (if not 0)
-	x86: `CMOV`.
-	Full predication
	-	ITANIUM.
	```
	MPEQZ p1, p2, R1
	(p2) ADD1 R2, R2, 1
	(p1) ADD1 R3, R3, 1
	```


## Summary
-	Need [[Computer Architecture|Compiler]] support.
-	Removes bad branches
-	Need more [[Instruction Register]]s.
-	More insts executed and wasted.