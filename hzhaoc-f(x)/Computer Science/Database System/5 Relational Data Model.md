## Ch5: Relational Data Model

![[ATTRIBUTES, TUPLES, RELATION NAME.png|600]]

_Some concepts_

- **Relation schema** can be interpreted as a **declaration** or a type of **assertion**. Then each **tuple** in the relation can be interpreted as a **fact** or **instance**.
- **Relation schema** can also be interpreted as a **predicate**. Then values in each tuple are values that **satisfy** the predicate.
- **Relation state:** a set of n-tuples where each tuple is an ordered list of n values, where each value is an element of corresponding **domain**.

_Notation_

- Relation schema R of degree n:
- Domain of :
- Relation state of relation schema R: r(R)

_Constraints_

- **Model-based** or **implicit constraints** : constraints that are inherent in the model.
- **Schema-based** or **explicit constraints** : constraints that are directly expressed in the schemas of the data model, typically specified in DDL.
- Application-based or semantic constraints or business rules: constraints specified by application programs.
- Domain constraints
  1. **Superkey:** A subset of attributes of a relation schema R with the property that each tuple in any relation state r of R is unique.
  2. **Key:** A minimal superkey. A relation schema may have more than one key. Such a key is also called **candidate key**. One of the candidate keys can be designated as the **primary key**.
- Relational database schemas

A relational database schema S is a set of relational schemas S = {}and a set of integrity constraints IC.

A **relational database state** DB of S is a set of relation states . A database state that does not obey all integrity constraints is **not valid**.

- Entity integrity, referential integrity, foreign keys

- Entity integrity constraint states that no primary key value can be NULL.
- **Referential integrity constraint** is specified between two relations and used to maintain the consistency among tuples in the two relations.

Formally, a set of attributes FK in relation schema is a foreign key of that references if following rules are satisfied:

1. FK attributes in have same domain(s) as the PK attributes of .
2. A value of FK in a tuple of the current state either equals a value of PK in a tuple of the current state , or is NULL. In the former case, **references** or **refers** to .

In this definition, is **the referencing relation** , is the **referenced relation**.

_Operations_

- Insert
- **Delete:** can only violate referential integrity constraint.
- Update/modify
- **Transaction:** an executing program that includes a set of database operations.