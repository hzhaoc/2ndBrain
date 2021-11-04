### Language Processing System Overview
![[language-processing system overview.jpg|400]]

Some language processors combiner **[[Computer Science/Programming/Compiler#Interpreter|Interpreter]]** and **[[Computer Science/Programming/Compiler|Compilers]]**. A high-level source program may be first converted to a intermediate program, like `__pyc__` for python, then a virtual-machine will compile the intermediary code immediately before run time.

### Structure of a [[Computer Science/Programming/Compiler|Compiler]]
- Analysis:
	- lexical analyzer/scanning
	- syntax analyzer
	- semantic analyzer
- Synthesis:
	- code generator (intermediate code -> machine code)

### Phases of a [[Computer Science/Programming/Compiler|Compiler]]
- lexical analyzer
- syntax analyzer
- semantic analyzer
- intermediate code generator
- machine-code generator

![[compiler structure.jpg|400]], ![[compiler structure 2.jpg|400]]