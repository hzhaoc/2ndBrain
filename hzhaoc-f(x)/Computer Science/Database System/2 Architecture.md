## **Ch2: DBMS concepts, architecture**
***Data Models***

A collection of concepts that can be used to describe the structure of a database – provides necessary means to achieve data abstraction.

**High-level** or **conceptual data models** provide concepts close to the way users perceive data.

**Low-level** or **physical data models** provide concepts close to how data is stored physically. 

**Implementation** or **representational data models** include **relational data model**, and old data models such as **network** and **hierarchical models**. New models include object data model. 

- **Relational data model** – main model used in current commercial
- **Object data model** – implemented in some commercial and not used widely yet
- **Tree-structure data model** – e.g. XML DBMS
- **Hierarchical** and **network data models** – legacy models

***Schema***

Description of database. A displayed schema is called **schema diagram**. 

- **Internal schema** – describes physical storage structure of the database
- **Conceptual schema** – describes structure of the whole database for a community of users
- **External schema** or **user views** – describes part of the database that a particular user group is interested in

***Data Independence***

- **Logical data independence** – the capacity to change conceptual schema without changing external schema or application programs
- ***Physical data independence –*** the capacity to change internal schema without changing conceptual schema.

***DBMS language***

- **Data Definition Language (DDL)** - specify both internal and conceptual schemas or only conceptual schema.
- **Storage Definition Language (SDL)** - specify internal schema**.**
- **View Definition Language (VDL)** - specify user views and mappings to the conceptual schema. Usually DDL is used to specify both conceptual and external schemas.
- **Data manipulation language (DML)** - to operate on database

***DBMS Architecture***

- **Centralized DBMSs architecture** – processing data, application program execution, user interface processing all on server machine.
- **Two-tier Client/Server architecture** – query on server, application program and user interface on client side. DBMS vendors provide **ODBC drivers (open database connectivity)** that provides an **API (application program interface)** which allows client programs to call DBMS. 
- **N-tier architectures for web applications –** middle layers are usually web/app server.

![[dbms_architecture.png]]
![[DBMS_modules.png]]

