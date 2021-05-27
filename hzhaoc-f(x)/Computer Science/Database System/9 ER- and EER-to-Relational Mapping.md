## Ch9: ER- and EER-to-Relational Mapping

_Purpose of this chapter:_

Learn how to design a relational database design based on a conceptual schema design. We focus on **logical database design** , namely **data model mapping**.

_9.1 ER-to-Relational mapping_

![[Mapping of regular entity types.png]]

_ **Step 1. Mapping of regular entity types** _

To walkthrough an example, for each strong entity type E in ER (Figure 9.1 is the diagram), we create EMPLOYEE, DEPARTMENT, and PROJECT as **entity relations** for strong entity types. Include only **simple component attributes**. Decide **primary keys**. Foreign keys and relationship attributes are not added yet. No multi-valued or derived attributes. The result is shown below.

![[eer_map_dbms1.png]]

_ **Step 2. Mapping of weak entity types** _

For each weak entity type W in the ER schema with owner entity type E, create a relation R and include all simple attributes (or simple components of composite attributes) as attributes of R.

In the example, we create the relation DEPENDENT for the weak entity type DEENDENDT. Primary key &quot;Ssn of EMPLOYEE will be foreign key of DEPENDENT Essn. Primary key of DEPENDENT will then be {Essn, Dependent\_name} where the later is a partial key.

![[eer_map_dbms2.png]]

_ **Step 3: Mapping of Binary 1:1 relationship type** _

Identify a binary 1:1 relationship E in ER diagram (MANAGES) -\&gt; choose one relation S (DEPARTMENT, better the one that has **total participation** ) -\&gt; include the primary key of the other relation T (EMPLOYEE) as foreign key in the S. We also include simple attribute (Start\_date) of the relationship in S.

_ **Step 4: Mapping of Binary 1:N relationship type** _

Identify a binary 1:N relationship type R in ER -\&gt; identify relation S at the N-side -\&gt; include as foreign key in S the primary key of the other relation T.

In the example, For WORKS\_FOR we include primary key Dnumber of DEPARTEMNET as foreign key in EMPLOYEE (Dno); for SUPERVISION we include primary key of EMPLOYEE as foreign key in EMPLOYEE itself in recursion (Super\_ssn); …

_ **Step 5: Mapping of Binary M:N relationship types** _

Identify a M:N relationship R in ER, relations S, T -\&gt; create a new relation S to represent it -\&gt; include as foreign key attributes in S the primary keys of S, T, the combined foreign keys in S will become the primary key of S. Also include any simple attributes of S.

In the example, for WORKS\_ON, we create a relation WORKS\_ON. We include primary keys of PROJECT and EMPLOYEE as foreign keys in WORKS\_ON, Pno and Essn. Also include Hours. Primary key of WORKS\_ON is {Essn, Pno}. The relation is shown below.

![[eer_map_dbms3.png]]

_ **Step 6: Mapping of Multivalued attributes** _

For each multivalued attribute A, create a new relation R. It will include an attribute corresponding to A, plus the primary key attribute K as a foreign key in R.

In the example, we create a relation DEPT\_LOCATION. Primary key is {Dlocations, Dnumber}. Note in newer relational models, multivalued attribute can be represented by an array in instead of creating a new table.

![[eer_map_dbms4.png]]

_ **Step 7: Mapping of N-ary relationship types** _

For each n-ary relationship where n\&gt;2, create a new relationship relation S. Include as foreign key attributes in S the primary keys of the relations participating R. Also include any simple attributes of S. Finally, primary key of S will be a combination of usually all its foreign keys. If one participating relation E has cardinality constraint of 1:1 or 1:N, then the corresponding foreign key will not be a primary key.

_ **Summary** _

**Correspondence between ER and Relational Models**

![[er_dbms_sum.png]]

Final relational schema for the example we walked through:

![[eer_map_dbms5.png]]

Note that in relational schema, compared to ER schema, relationship types are not always represented explicitly; instead, they are represented by either attributes (foreign keys and primary keys from participating relations) or separate relations.

_9.2 Mapping EER to relations_

_ **Step 8: mapping specialization or generalization** _
- _Option a –_ _mandatory disjoint subclasses_ _-\&gt; subclass relations only_
- _Option b_ _– mandatory overlap / non-mandatory overlap / non-mandatory disjoint subclasses_ _-\&gt; multiple relations for subclass and parent class_
- _Option c – single relation with an additional field &#39;type&#39;(indicating subclass)._ _This works when subclasses are disjoint__._
- _Option d – single relation with multiple fields to indicate types. Create a relation with where each tuple is a binary integer or Boolean type attribute indicating whether or it belongs to correspondent subclass._ _This works for subclasses that are overlapping or disjoint__._

By the way for shared subclasses, they must have the same key attribute. Option c and d work for them.

_**Step 9: Mapping union types (categories)**_

For unions whose superclasses have different keys, create a relation to represent the union -\&gt; create a new key attribute as **surrogate key**. For unions whose superclasses have same keys, there is no need for surrogate key. Example is illustrated below (OWNER, REGISTERED\_VEHICLE are unions).

![[eer_map_dbms6.png]]