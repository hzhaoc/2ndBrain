## Ch4: Enhanced Entity-Relationship (EER) model

_Inheritance, subclass/superclass_

- **Subclass/superclass relationship**
- **Generalization/specialization**
- **Attribute inheritance**

_Constraints of specialization/specialization_

- **Predicate-defined specialization**
- **Attribute-defined specialization:** All subclasses in a specialization have their membership condition on the same attribute of the superclass.
- **User-defined:** membership in subclass is determined by user.
- **Disjointness constraint**
- **Completeness** or **totalness constraint:** a total specialization constraint specifies that every entity in the superclass must be a member of at least one subclass in the specialization.
- ![[EER DIAGRAM NOTATION FOR OVERLAPPING DISJOIN TOTAL SPECIALIZATION SUBCLASS SUPERCLASS.png]]

_Specialization Hierarchies, Lattices_

A specialization hierarchy has the constraint that every subclass has only one superclass – namely a tree structure or strict hierarchy. In contrast, a specialization lattice has the constraint that a subclass can have more than one superclass.

_Specialization vs generalization_

Specialization is often used in top-down conceptual refinement; generalization is often used in bottom-up conceptual synthesis.

_Union Type (Category)_

A category holds a subset of union of its superclasses.

A member in category must exist in only one of its superclasses. A category can be **total** or **partial**. A total union case can be converted total disjoint specialization case.