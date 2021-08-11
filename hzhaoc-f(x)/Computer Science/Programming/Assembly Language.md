In computer programming, **assembly language** (or **assembler language**), is any low-level programming language in which there is a very strong correspondence between the instructions in the language and the architecture's [[Machine Code]] [[Instruction Set Arch.#Instruction|instructions]].

Assembly code is converted into executable machine code by a utility program referred to as an _assembler_. The conversion process is referred to as _assembly_, as in _assembling_ the source code. Assembly language usually has one statement per machine instruction (1:1), but comments and statements that are assembler directives and symbolic labels of program and memory locations are often also supported.

Each assembly language is specific to a particular [[Computer Architecture]] and sometimes to an [[Operating System]]. However, some assembly languages do not provide specific syntax for operating system calls, and most assembly languages can be used universally with any operating system, as the language provides access to all the real capabilities of the [[CPU|processpor]], upon which all system call mechanisms ultimately rest. In contrast to assembly languages, most high-level programming languages are generally portable across multiple architectures but require interpreting or [[Computer Science/Programming/Compiler|compiling]], a much more complicated task than assembling.

# Syntax
Assembly language uses a mnemonic to represent each low-level [[Machine Code]] or [opcode](https://en.wikipedia.org/wiki/Opcode "Opcode"), typically also each [[Storage Hierarchy#Instruction Register|Architecture Register]], flag, etc. Many operations require one or more operands in order to form a complete instruction. Most assemblers permit named constants, registers, and labels for program and memory locations, and can calculate expressions for operands. Thus, the programmers are freed from tedious repetitive calculations and assembler programs are much more readable than machine code. Depending on the architecture, these elements may also be combined for specific instructions or [addressing modes](https://en.wikipedia.org/wiki/Addressing_mode "Addressing mode") using offsets or other data as well as fixed addresses. Many assemblers offer additional mechanisms to facilitate program development, to control the assembly process, and to aid debugging.

# example
```
MOV AL, 1h        ; Load AL with immediate value 1
MOV CL, 2h        ; Load CL with immediate value 2
MOV DL, 3h        ; Load DL with immediate value 3
```
The syntax of MOV can also be more complex as the following examples show.
```
MOV EAX, [EBX]	  ; Move the 4 bytes in memory at the addr in EBX into EAX
MOV [ESI+EAX], CL ; Move the contents of CL into the byte at address ESI+EAX
MOV DS, DX        ; Move the contents of DX into segment register DS
```
In each case, the MOV mnemonic is translated directly into one of the opcodes 88-8C, 8E, A0-A3, B0-BF, C6 or C7 by an assembler, and the programmer normally does not have to know or remember which.