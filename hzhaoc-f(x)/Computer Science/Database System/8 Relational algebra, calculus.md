## Ch8: Relational algebra, calculus

_Relational Algebra_

The basic set of operations for a formal relational model is the **relational algebra**. A sequence of relational algebra forms a **relational algebra expression**. Operations are divided into two groups: 1. Set operations from math set theory, like UNION, INTERSECTION, SET DIFFERENCE… 2. Operations for relational databases like SELECT, PROJECT, JOIN.

- Unary relational operations: SELECT, PROJECT
  1. SELECT: choose rows from tables. Operator:
  2. PROJECT: choose columns from tables (projected **relations are sets** ). Operator:
  3. Rename: **p**

$$\rho_{RUser[Year,BirthYear,GenderSex]}(RegularUser)$$

- Relational algebra operations from set theory
  1. Union:
  2. Intersection:
  3. Set diff/minus **\\** (in relational calculus:  **and not**)
  4. Cartesian product (cross product): **X**
  5. 
- Binary relational operations
  1. Natural join **:** operator: **\***
  2. Theta join
  3. Outer join
  4. Divideby

_Relational Calculus_

**Relational calculus** provides a higher-level declarative language for specifying relational requires. Two variations: 1. **Tuple** relational calculus. 2. **Domain** relational calculus. Relational calculus is based on math logic branch **predicate calculus.**

- Tuple relational calculus
	- Range expression:
	- Attribute value:
	- Selection
	- Projection
	- Union
	- Interception
	- Set diff
	- Natural join
	- Cross product
	- Divideby
- Domain relational calculus.