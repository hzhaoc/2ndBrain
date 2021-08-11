# Divide and Conquer
In computer science, divide and conquer is an algorithm design paradigm. **A divide-and-conquer algorithm recursively breaks down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly. The solutions to the sub-problems are then combined to give a solution to the original problem.**

Designing efficient divide-and-conquer algorithms can be difficult. As in mathematical induction, it is often necessary to generalize the problem to make it amenable to recursive solution. The correctness of a divide-and-conquer algorithm is usually proved by **mathematical induction**, and its computational cost is often determined by solving recurrence relations.

# Greedy
A greedy algorithm is any algorithm that follows the **problem-solving heuristic of making the locally optimal choice at each stage**. In many problems, a greedy strategy does not produce an optimal solution, but a greedy heuristic can yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time.

# Dynamic Programming
Dynamic programming is both a mathematical optimization method and a computer programming method. The method was developed by Richard Bellman in the 1950s and has found applications in numerous fields, from aerospace engineering to economics.

In both contexts it refers to simplifying a complicated problem by breaking it down into simpler sub-problems in a recursive manner. While some decision problems cannot be taken apart this way, decisions that span several points in time do often break apart recursively. Likewise, in computer science, **if a problem can be solved optimally by breaking it into sub-problems and then recursively finding the optimal solutions to the sub-problems, then it is said to have [Optimal Substructure](https://en.wikipedia.org/wiki/Optimal_substructure)**.

If sub-problems can be nested recursively inside larger problems, so that dynamic programming methods are applicable, then there is a relation between the value of the larger problem and the values of the sub-problems. In the optimization literature this relationship is called the **Bellman equation**.