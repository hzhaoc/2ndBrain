Bloom Filter
============

1.  A variant of [[Hash Table]] to Test whether an element is a member of a
    set. For examples, checking availability of username in
    registration.

2.  How it works: Given data set S:
	1. Choose hash functions, number = K.
	2. Allocate fixed number of total bits in memory for the dataset. Total
    bits = n. So for each of the element in S, allocated number of bits
    are b = n/S.
	3. Insertion: (when a new element is added) Set each hash value of the K to 1. $\text{Hash}_{i}\left( j \right) = \ 1,\ i\  = \ 1,\ 2,\ \ldots,\ K.$ where j is the new element key from input
	4.  Lookup: If all hash values of the element j that's to be lookup = 1, then it's in the data structure, else not.

	5.  Working space of Bloom Filter is like the following table:

		  | array of bits | 0 |  0 |  0 |  0 |  0 |  0 |  0 |  0 |  0 |  0|
		  | ------------ | -- | -- | -- | --| -- | -- | -- | -- | -- | --|
		  | hash            |  1   | 2  | 3  | 4 |  5 |  6 |  7 |  8 |  9 |  10|

3.  Pros & Cons

    1. Pro: More space-efficient than hash-tables.

    2. Con: Can't store an associated object

    3. Con: No deletions

    4. Small false positive probability

    5. **Can only check key's existence (0/1), not lookup key's
        value**

4.  Trade-off between error (false positive) and improved memory space
    allocation

-   Assumption

> All hash function $h_{i}\left( x \right),\ i\  = 1,\ 2,\ \ldots,\ K$
> hash random keys and uniformly distribute hashes in the array table.

-   Setup

    -   Storage space: array A of n bits, one bit per hash value

    -   Input data set S that's inserted, length = S

-   Analysis

> Denote Set A as the array,
> $A_{1},\ A_{2},\ A_{3},\ \ldots,\ A_{n}, = \ \ 0\ or\ 1$

$$P\left( A_{i} = \ 1 \right) = 1 - \left( 1 - \frac{1}{n} \right)^{K\left| S \right|},\ \forall\ i \in 1,\ 2,\ 3,\ \ldots,\ n$$

> Because $e^{- \frac{1}{n}} > 1 - \ \frac{1}{n}$

$$P\left( A_{i} = \ 1 \right) \leq 1 - e^{- \frac{1}{n}K\left| S \right|},\ \forall\ i \in 1,\ 2,\ 3,\ \ldots,\ n$$

> Let b to be number of bits allocated to each object in input set S:
>
> $b = \ \frac{n}{S}$ \> 0
>
> Therefore,

$$P\left( A_{i} = \ 1 \right) \leq 1 - e^{- \frac{K}{b}},\ \forall\ i \in 1,\ 2,\ 3,\ \ldots,\ n$$

> So $for\ x \notin S,$

$$p\left( \text{false\ positive\ of\ x} \right) = \ \coprod_{i = 1}^{K}{P\left( h_{i}\left( x \right) = 1 \right)} \leq \ \left\lbrack 1 - \ e^{- \frac{K}{b}} \right\rbrack^{K},\ \forall\ x \notin S$$

> **Objective**

$$\min{p\left( \text{false\ positive\ of\ x} \right)},\ \forall\ x \notin S$$

$$\min\left\lbrack 1 - \ e^{- \frac{K}{b}} \right\rbrack^{K},\ \forall\ x \notin S,\ K \geq 1,b \geq 1$$

> Set b constant, (what's usually determined or if not, to find
> relationship between K and b), and define:

$$f\left( x \right) = \left\lbrack 1 - \ e^{- \frac{x}{b}} \right\rbrack^{x},x \geq 1,b \geq 1$$

> First derivative:
>
> $f^{'}\left( x \right) = e^{ln(1 - e^{- \ \frac{x}{b}})x}\lbrack\frac{e^{- \ \frac{x}{b}}*\frac{1}{b}*x}{1 - e^{- \frac{x}{b}}} + ln(1 - e^{- \ \frac{x}{b}})\rbrack$,
> x\>=1, b\>=1
>
> Note the left part of the left formula

$$e^{ln(1 - e^{- \ \frac{x}{b}})x} > 0$$

> We only need right part of the left formula to know f(x) monotony.
>
> Define:

$$g\left( x \right) = \frac{e^{- \ \frac{x}{b}}*\frac{1}{b}*x}{1 - e^{- \frac{x}{b}}} + \ln\left( 1 - e^{- \ \frac{x}{b}} \right),\ x > = 1,\ b > = 1$$

> Let:

$$y = 1 - \ e^{- \ \frac{x}{b}},x \geq 1,b \geq 1$$

> So:

$$g\left( y \right) = \ln{{\lbrack\left( 1 - y \right)}^{\frac{y - 1}{y}}*y}\rbrack,y\  \in (0,\ 1)$$

> In order to know f(x) monotony, we only need to know g(y) range.
>
> Namely to know range of:

$$h\left( y \right) = \left( 1 - y \right)^{\frac{y - 1}{y}}*y - 1,y \in (0,1)$$

> To know range of h(y), let's try looking at its monotony by its first
> derivative:

$$h^{'}\left( y \right) = \frac{1}{y}*e^{\ln\left( 1 - y \right)*\frac{y - 1}{y}}*\left\lbrack 2y\  + \ln\left( 1 - y \right) \right\rbrack,\ y \in (0,1)$$

> Note left part of the right side of equation:

$$\frac{1}{y}*e^{\ln\left( 1 - y \right)*\frac{y - 1}{y}} > 0$$

> Define:

$$k\left( y \right) = 2y\  + \ln\left( 1 - y \right),\ y\  \in (0,\ 1)$$

> Then its first derivative:

$$k^{'}\left( y \right) = - \frac{1}{1 - y} + 2,\ y \in (0,1)$$

> Easily know:

$$k^{'}\left( \frac{1}{2} \right) = 0$$

$$k^{'}\left( y < \frac{1}{2} \right) > 0$$

$$k^{'}\left( y > \ \frac{1}{2} \right) < 0$$

> There for:

1.  $k\left( y \right)\text{\ monotonically\ increase\ at\ }\left( 0,\ 0.5 \right),\ monotonically\ decrease\ at\ \left( 0.5,\ 1 \right)$

$$2.\ \max{k(y)},y \in \left( 0,\ 1 \right) = k\left( 0.5 \right) = \sim 0.3(approximate)$$

> Note that there's a number between 0.5 and 1 that make the function
> equal to zero,
>
> Denote it as a constant a, so:

$$1 > \ a > 0.5$$

$$k\left( a \right) = 0$$

> By extreme value we know:

$$k\left( y \right) > 0,\ y \rightarrow 0$$

> Therefore,

$$k\left( y \right) > 0,\ y \in (0,\ a)$$

$$k\left( y \right) < 0,y \in (a,1)$$

> Namely,

$$h'\left( y \right) > 0,\ y \in (0,\ a)$$

$$h'\left( y \right) < 0,y \in (a,1)$$

> Namely,

$$h\left( y \right)\text{\ monotonically\ increase\ at\ }\left( 0,\ a \right),\ and\ monotinically\ decrease\ at\ \left( a,\ 1 \right),\ $$

$$where\ a\ is\ a\ constant\ and\ 1 > a > 0.5\ $$

> Obviously:

$$h\left( 0.5 \right) = 0$$

> So,

$$h\left( y \right) < 0,\forall\ y \in (0,\ 0.5)$$

> Consider when 1 \> y \> 0.5,

$$h\left( y \right) = \ \left( 1 - y \right)^{\frac{y - 1}{y}}*y - 1,y \rightarrow 1$$

$$h\left( y \right) = \ \left( 1 - y \right)^{\frac{y - 1}{y}} - 1,y \rightarrow 1$$

$$h\left( y \right) = \frac{1}{{(1 - y)}^{1 - y}} - 1,\ y \rightarrow 1$$

$$h\left( y \right) \rightarrow 0$$

> Therefore,

$$h\left( y \right) > 0,\ \forall\ y \in \ \left( 0.5,\ 1 \right),\ *not\ a\ very\ strict\ proof$$

> To sum up,

$$h\left( y \right) < 0\ \forall\ y \in \left( 0,\ 0.5 \right),\ h\left( y \right) = 0\ for\ y = 0.5,\ h\left( y \right) > 0\ \forall\ y \in (0.5,\ 1)$$

> Obviously,

$$g\left( y \right) < 0\ \forall\ y \in \left( 0,\ 0.5 \right),\ g\left( y \right) = 0\ for\ y = 0.5,\ g\left( y \right) > 0\ \forall\ y \in \left( 0.5,\ 1 \right)$$

> Namely,

$$f'\left( y \right) < 0\ \forall\ y \in \left( 0,\ 0.5 \right),\ f'\left( y \right) = 0\ for\ y = 0.5,\ f'\left( y \right) > 0\ \forall\ y \in (0.5,\ 1)$$

> Namely,

$$f(y)\ monotically\ decrease\ at\ \left( 0,\ 0.5 \right),\ and\ monotically\ increase\ at\ (0.5,\ 1)$$

> Therefore,

$$\min{f\left( y \right)} = f\left( 0.5 \right)$$

> Therefore,

$$1 - \ e^{- \ \frac{x}{b}} = 0.5$$

> So,

$$x = ln2*b$$

> In all, when number of hash functions K = ln2 \* b (number of bits
> allocated per object key), (ln2 = \~0.693). Then,

$$p\left( \text{false\ positive\ of\ x} \right) \leq \ \left( \frac{1}{2} \right)^{(ln2)b},\ \forall\ x \notin S$$

> Bloom Filter's false positive rate for new insert x is at its minimum
> (S is inserted already).
