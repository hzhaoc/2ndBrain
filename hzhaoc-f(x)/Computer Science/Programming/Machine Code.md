In computer programming, **machine code**, consisting of **machine language** [[Inst Set Arch.|instructions]], is a low-level programming language used to directly control a computer's [[CPU]]. Each instruction causes the CPU to perform a very specific task, such as a load, a store, a jump, or an [[CPU#ALU|ALU]] operation on one or more units of data in the CPU's [[Memory & Storage#Instruction Register|registers]] or [[Memory & Storage#RAM DRAM|memory]]

# example
The [MIPS architecture](https://en.wikipedia.org/wiki/MIPS_architecture "MIPS architecture") provides a specific example for a machine code whose instructions are always 32 bits long. The general type of instruction is given by the _op_ (operation) field, the highest 6 bits. J-type (jump) and I-type (immediate) instructions are fully specified by _op_. R-type (register) instructions include an additional field _funct_ to determine the exact operation. The fields used in these types are:
```
   6      5     5     5     5      6 bits
[  op  |  rs |  rt |  rd |shamt| funct]  R-type
[  op  |  rs |  rt | address/immediate]  I-type
[  op  |        target address        ]  J-type
```
_rs_, _rt_, and _rd_ indicate register operands; _shamt_ gives a shift amount; and the _address_ or _immediate_ fields contain an operand directly.

For example, adding the registers 1 and 2 and placing the result in register 6 is encoded:
```
[  op  |  rs |  rt |  rd |shamt| funct]
    0     1     2     6     0     32     decimal
 000000 00001 00010 00110 00000 100000   binary
```
Load a value into register 8, taken from the memory cell 68 cells after the location listed in register 3:
```
[  op  |  rs |  rt | address/immediate]
   35     3     8           68           decimal
 100011 00011 01000 00000 00001 000100   binary
```
Jumping to the address 1024:
```
[  op  |        target address        ]
    2                 1024               decimal
 000010 00000 00000 00000 10000 000000   binary
```

