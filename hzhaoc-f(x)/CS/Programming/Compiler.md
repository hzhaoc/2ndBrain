### Compiler, Interpreter

1.  Compiler
Compiler is a program that reads a source program written in the
high-level language and converts it into the machine code (or CPU
understandable bytecode?) or low-level language and reports errors
present in the program. It converts the entire source code in one go or
multiple passes, into compiled object code ready for execution.

1.  Phases of compiler

    1.  Lexical Analyzer

    2.  Syntax Analyzer

    3.  Semantic Analyzer

    4.  Intermediate Code Generator

    5.  Code Optimizer

    6.  Code Generator

2.  Interpreter
Interpreter is an alternative for implementing a programming language
and does the same work as a compiler. Interpreter performs **lexing**,
**parsing**, and **type checking** similar to a compiler. But
interpreter **processes syntax tree directly to access expressions and
execute statement** rather than generating code from the syntax tree.

3.  Compiler vs Interpreter

 |   | Compiler |  Interpreter |
 |---|---|----|
 |Description | A translator which transforms source language (high-level language) into object language (machine language).| A program which imitates the execution of program written in a source language.|
  |Input|    Convert the whole program in one go |   Converts the program line by line|
  |Output|   Generates intermediate object code, e.g. pyc File  | Does not produce any intermediate object code |
  |Working Mechanism  | Compilation done before execution  | Compilation and execution take place simultaneously|
  |Speed | Faster |  Slower |
  |Memory  |  Bigger due to creation of object code  | Less due to no creation of object code |
  |Errors|  Display errors all at once after compilation |  Display errors line by line |
  | Pertaining Programming Languages | C, C++, C\#, Scala, typescript | PHP, Perl, Python, Ruby |

Compilation and interpretation can be combined to implement a
programming language. In which a compiler generates low-level code then
the code is interpreted rather than compiled to machine code.

For instance, Python is a 'COMPILED INTERPRETED' language, meaning when
Python program is run:

1.  First python checks for program syntax.

2.  Second compiler compiles program, converting it to bytecode and the
    bytecode is loaded in system memory. (The bytecode is a
    **platform-independent representation of source code**. And note
    that Python bytecode is **not binary machine code**). If the python
    program is already compiled (there's a pyc. file in file system and
    memory), python automatically checks the timestamps of source code
    and bytecode to recompile. If the python program is saved, python
    automatically recreated bytecode

3.  Third compiled bytecode is interpreted from memory to execute in
    Python Virtual Machine (PVM). (PVM is the **runtime engine** of
    Python, as part of Python system. It's the component that truly runs
    our scripts. And it's the last step of what is called the **Python
    interpreter**.)

#### Compiler Optimization
1.  String interning
String Interning: When compiler is compiling, it uses the string that
already exists if the string is under some specific conditions, pointing
to the same object in memory, saving memory space. These conditions include:
- The string must be a constant at compile time, including
    expressions.
	(Expression is evaluated before an object is instantiated.)
- The string is subject to constant folding (and no longer than 20
    characters?)

> Constant folding here refers to evaluating constant expressions at
> compile time rather than computing them at runtime. However it seems
> the '20-character' condition doesn't apply to my running Python file.
> My CPython doesn't have this condition?

- The string must consist exclusively of ASCII letters, digits, or
    underscores.

- The string is empty no matter it is under the three conditions above
    or not.

2.  Constant Folding
Constant folding is the process of recognizing and evaluating constant
expressions at compile time rather than computing them at runtime. (Is a
kind of peephole optimization technique?)

3.  Shared objects
When a python program is initialized, the Unicode characters 0 -- 256
and integers 0 -- 256 are loaded as shared objects, and behave
identically to interned strings.