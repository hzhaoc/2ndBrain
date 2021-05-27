## **Ch10: SQL Programming (C/C++, Java)**

_Approaches to Data Base Programming_

- **Embedded SQL**

Embed SQL commands in a host language that are identified by precompiler or preprocessor using like prefix.

- ( **API** ) Library of database functions or classes

Actual SQL commands will be included as parameters in these function calls.

- Design a new language

_Impedance Mismatch_

- Mismatched data types for host languages, database languages – needs binding.
- Mapping database table (if relational database) to correct data structure in host language

_Embedded SQL_

- With C: Declare sections, Cursor
- With Java: SQLJ.

_API (libraries)_

SQL/CLI:SQL Call Level Interface.

- With C: sqlcli.h
- With Java: load a Java Database Connectivity driver (usually referred to as JDBC driver)

_Database Stored Procedures_

_Permanent procedures stored at server where the database is located_

_SQL/PSM_

SQL/Persistent Stored Modules can be used to write stored procedures. It is an example of a database programming language that extends a database model and language – SQL – with programming language constructs, such as **conditional statements** and **loops**.

_Compare_

- Embedded SQL
  1. Pros: More readable, more visible. SQL queries run at compile time. Easier.
  2. Cons: loss of flexibility.
- API
  1. Pros: more flexible
  2. Cons: more complex
- Design a new language
  1. Pros: no Impedance Mismatch
  2. Cons: overheads of learning new language
