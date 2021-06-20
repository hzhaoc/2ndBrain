## **Ch15: Relational Database Further Dependencies**

_Inference Rules for Functional Dependencies_

An FD X -\&gt; Y is inferred from or implied by a set of dependencies F specified on R if X -\&gt; Y holds in every legal relation state r of R; that is, whenever r satisfies all the dependencies in F, X-\&gt;Y also holds in r.

Inference rules:

- IR1 (reflexive rule):
- IR2 (augmentation rule): Z
- IR1 (transitive rule):

Following from IR1,2,3:

- IR4 (decomposition or projective rule): if X-\&gt;YZ, then X-\&gt;Y
- IR5 (union or additive rule): if X-\&gt;Y, X-\&gt;Z, then X-\&gt;YZ
- IR6 (pseudo-transitive rule): if X-\&gt;Y, WY-\&gt;Z, then WX-\&gt;Z

![[equivalence sets of functional dependencies.png|600]]

_FD compare, minimal set, minimal cover_

_Properties of Relational Decompositions_

- Dependency preservation of Decomposition
- Nonadditive Join Property of a Decomposition