### Comparator/Sorting Network
[Comparator networks](https://en.wikipedia.org/wiki/Sorting_network) is a special type of circuits of lines that compare two input and sort it by swapping or not swapping the two inputs.
![[comparator network.png|300]]

### Bitonic Sequence
a sequence ${a1,a2,...,an}$ is bitonic if:
- $a1\leq a2\leq a3,...,\leq ai$ and $ai+1\geq ai+1\geq ai+3,...,\geq an$, $\exists i \in [1,n]$
- or above holds after some circular shifts

Visual:
![[bitonic sequence.png|400]]

##### Bitonic Splits
A bitonic split is to reorder a bitonic sequence $a1,a2,a3,...,an$ by $(a_1,a_{n/2}),(a_2,a_{n/2+1}),...,$. This split the original bitonic sequence into two smaller bitonic sequences where the max of one sequence is not greater than the min of the other sequence. Shown below. This makes it very suitable for parallelism and divide and conquer.
![[bitonic split 1.png|400]] ![[bitonic split 2.png|400]] ![[bitonic split 3.png|400]]

- A parallel scheme of bitonic scheme using comparator networks
![[bitonic split parallel scheme.png|600]]

##### Bitonic Merge
Using bitonic splits recursively, we can sort a bitonic sequence.
![[bitonic merge.png|600]]

- Generate a bitonic sequence: to generate a bitonic sequence to do such a merge:
	1. Start with an arbitrary input.
	2. Run plus/minus bitonic merges of size 2.
	3. Run plus/minus bitonic merges of size 4.
	4. continue until done.

##### Bitonic Sort
For any random array, we can first generate a bitonic sequence, then does bitonic merge to sort the random array.
![[bitonic sort.png|600]]

example:
![[bitonic sqe gen.png|500]]

Pros: 
- The bitonic merge has a fixed regular structure that lends itself to a natural implementation with a programmable gate array, etc. 
- It also means it will map well to fixed data parallel hardware like SIMD, etc.

Cons: 
- It is NOT work optimal. So trade-offs will have to be made.