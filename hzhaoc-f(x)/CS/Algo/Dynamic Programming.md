Dynamic Programming
===================

1.  Principles
    ----------

    -   Identify subproblems

    -   Solve 'larger' subproblems given 'smaller' subproblems'
        solutions

    -   Compute final solution from solutions to all subproblems

2.  MWIS - compute maximum independent set in graph
    -----------------------------------------------

    -   Denote Gi = first 1 vertices of graph G, A\[i\] = value of max
        Independent Set of Gi

    -   Initialize A\[0\] = 0, A\[1\] = w1

    -   Loop i = 2, 3, ..., n:

> A\[i\] = max{a\[i-1\], a\[i-2\] + wi

3.  Knapsack problem
    ----------------

4.  Sequence alignment
    ------------------

5.  Optimal Binary Search Tree
    --------------------------

	O(n\^3) run time.

Bellman Ford (shortest path length)
-----------------------------------

-   Either compute a shortest path s-v or output a negative cycle

-   Let $L_{i,v}$ = minimum length of a s-v path with \<= i edges,
    cycles allowed, and $+ \infty$ if not such path exists
	For i = 1, 2, ..., n-1: (n if negative cycle existence needs to be checked)
	For v = 1, 2, ..., n:
	$$L_{i,v}\left\{ \begin{matrix}
	L_{\left( i - 1 \right),\ v} \\
	\min_{(w,v) \in E}\left\{ L_{\left( i - 1 \right),w} + _{\text{wv}} \right\} \\
	\end{matrix} \right.\ $$

-   Time Complexity is O(mn without negative edges.

-   Space Complexity: O(n\^2)

-   Space optimization: only need A\[i-1, v\] to compute A\[i, v\] for
    any v in vertexes

-   Predecessor pointers B\[i, v\]:

    -   For non-negative cycles: second-to-last vertex in the shortest
        path, B\[0, v\] = null

    -   For a negative cycle: use DFS to check for a cycle of
        predecessor pointers at every iteration

-   Modifications

    -   Toward a routing protocol: Switch from source-driven to
        destination-driven. Examples: RIP, RIP2.

    -   Handling asynchrony: switch from 'pull-based' to 'push-based',
        as soon as A\[i,v\] \< A\[i-1, v\], v notifies all of its
        neighbors. Facts: algorithm guaranteed to converge eventually,
        assuming no negative cycles.

    -   Handling failures -- when an edge is broken

> Fix: each v maintains an entire shortest path to destination, not just
> the next hop
>
> Con: more space required

Floyd-Warshall Algorithm (All-pairs shortest paths, APSP)
=========================================================

-   Goal: compute all pairs of shortest u-\>v path or report relevant
    negative cycles

-   Other algorithm running time:

O(n\^2\*m) for Bellman Ford,

O(nmlogn for Dijkstra

-   Floyd-Warshall Algorithm

    -   O(n\^3) running time

    -   Works with negative edges

    -   at least as good as n Bellman Fords, better in dense graph

    -   with nonnegative edge costs, competitive with n Dijkstra's in
        dense graphs

    -   important special case: transitive closure of a binary relation

Johnson's Algorithm (for APSP, all-pairs-shortest-paths)
========================================================

-   1 invocation of Bellman Ford + n invocation of Dijkstra: O(mnlogn)

-   Weight each vertex, adjust edge length to E(u, v) = E + Pu -- Pv

-   Weighting vertex, updating edge lengths: (add a new vertex, 1
    Bellmon Ford), can still report a negative cycle in original graph

-   N Dijkstra

-   5: For each pair u, v in G, return the shortest path distance
    d(u, v) = d'(u, v) -- pu + pv

-   Running time: O(1) in step 1, O(mn) in step 2, O(m) in step 3,
    O(nmlogn) in step 4, O(n\^2) in step 5, total: O(nmlogn).

-   Pro: **handle negative edges, and much better than FloydWarshall,
    BellmanFord in sparse graphs**

# Summary: Running time for APSP:

- Bellman Ford: O(n\^2\*m)
- Dijkstra: O(mnlogn) negative edges not allowed
- Warshall: O(n\^3)
- Johnson's: O(mnlogn)

**For sparse graph, Johnson is best; for dense graph, Floyd-Warshall is
best.**
