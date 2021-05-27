## **Ch1: Intro, Users**
***Database***

A database is a logically coherent collection of data with some inherent meaning. It represents some aspect of the real world.

***DBMS***

A database management system is a computerized system that enables users to create and maintain a database. It is a general-purpose software system that facilitates the processes of defining, constructing, manipulating, and sharing databases among users and applications.

***Design***

Design steps of a new application for an existing database or design of a new database: **requirements specification and analysis -> conceptual design (e.g. EER) -> logical design -> physical design.** 

***Data abstraction***

Program-data independence: Structure of data files is stored in the DMBS separately from the access programs. Program-operation independence: User applications can operate on data by invoking operations regardless of how operations are implemented.

***Actors on the scene***

- Database Administrators (DBA)
- Manage user access to database
- Fine-tune database efficiency. Responsible for low-efficiency issues.
- Manage security
- Design internal schema
- Design DDL (Data definition language)
- Database designers
- Identify data
- Structure data
- Communicate with users to create design, develop **views.**
- Usually part of DBA
- End users
- Casual end users: occasionally access the database, use query interface, like managers or browsers.
- Naïve or parametric end users: constantly query database, using programmed operations (**canned transactions**), like bank customers.
- Sophisticated end users: implement their own applications, like engineers.
- Standalone users: maintain personal databases by using software, like financial software user.
- Software engineers

**System analysts** develop **canned transactions** for users. **Application programmers** implement **canned transactions** as programs.

***Workers behind the scene***

- DBMS system designers and implementers

Design and implement DBMS modules and interfaces as a software package.

- Tool developers

Design and implement ***tools*** – the software packages that are optional packages to improve database design, modeling, performance.

- Operators and maintenance personnel.

Responsible for actual running and maintenance of the hardware and software environment for DBMS.

***DBMS advantages***

- Control data redundancy.
- Store all data in one place, known as **data normalization.** It ensures consistency and saves storage space. 
- Allow controlled redundancy to improve performance, known as **data denormalization**.
- Control DBMS access.
- Provide persistent storage for program objects
- Provide storage structures and search techniques for efficient query processing
- Provide backup and recovery
- Provide multiple user interfaces
- Represent complex relationships among data
- Enforce **integrity constraints**
- Referential integrity constraint
- Uniqueness or key constraint
- Business rules
- Permit inferencing and actions using rules and triggers

Change **deduction rules** rather than recode **procedural programs** to update **rules**, or associate **triggers** (form of a rule) with tables to update **rules**.

- Additional implications
- Enforce standards
- Reduced application development time
- Flexibility
- Up-to-date information
- Economies of scale



