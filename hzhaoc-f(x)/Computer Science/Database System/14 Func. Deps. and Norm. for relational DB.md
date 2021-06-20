## **Ch14: Functional Dependencies and Normalization for relational databases**

_Design Guideline 1_

Design a relation schema so that it is easy to explain its meaning.

_Design Guideline 2_

Design the base relation schemas so that no insertion, deletion or modification anomalies are present in the relations.

_Design Guideline 3_

Avoid placing attributes in a base relation whose values may frequently be NULL. If NULLs are unavoidable, make sure they are rare cases.

_Design Guideline 4_

Design relation schemas so that they can be joined with equality conditions on attributes that are appropriately related (primary key, foreign key) pairs.

_Functional Dependency_

In a relation schema R(r1, r2, …, rn), for any two tuples of t1 and t2 that have t1[X] = t2[X], where X is a subset of attributes of schem R, they must also agree on their another subset of attributes Y, meaning t1[Y] = t2[Y], thus Y is **functionally dependent** on X.

_Normal Forms, Normalization of Relations_

- **Definition**

The **normal form** of a relation refers to the highest normal form condition that it meets, and hence indicates the degree to which it has been normalized. It doesn&#39;t guarantee a good database design. Need two additional properties as follows:

- **Nonadditive join or lossless join property**

Must be achieved at any cost. How to preserve lossless join: ensure one of the join party is joined on its key

- **Dependency preservation property**

Can be sacrificed.

_**First Normal Form (1NF)**_

1NF disallows multivalued or composite attributes, allow only atomic values for attributes.

_**Second Normal Form (2NF)**_

A relation schema R is in 2NF if every nonprime attribute (attribute that&#39;s not a member of candidate key) A in R is **fully functionally dependent** on the any key of R. **No**** partial dependency**.

_**Third Normal Form (3NF)**_

According to Codd&#39;s original definition, a relation schema R is in 3NF if it satisfies 2NF and no nonprime attribute of R is transitively dependent on any key. (transitive dependency: X -\&gt; Z, and Z -\&gt; Y, Y is nonprime attribute of R, X is prime attribute, Z is nonprime attribute). **No transitive dependency.**

_**Boyce-Codd Normal Form (BCNF)**_

Based on 3NF, every determinant of functional dependencies is a candidate key

_ **Multivalued Dependency and Fourth Normal Form** _

_ **Join Dependencies and Firth Normal Form** _