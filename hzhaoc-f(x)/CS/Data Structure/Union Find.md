Union-find
==========

1.  Normal

-   Property

    -   Each data belongs to a group/cluster/union/leader

    -   Leader is the parent vertex

-   Merge/Union optimize

    -   in each merge, update the smaller group's leader

-   Pros & Cons

    -   Find() takes O(1)

    -   Union() worst case takes O(n)

    -   In MST, total Union() operations is O(nlogn)

2.  Lazy Unions

-   Property

    -   Update only one pointer in each union merge/fuse by making one
        group's leader a child of the other one

    -   Leader is the root vertex

-   Merge/Union optimize

    -   Union by rank.

> S1 = Find(x), S2 = Find(y). if rank(S1) \> rank(S2), then set
> parent\[S2\] to S1 vice versa

-   Update ranks to restore invariant
-   Path compression to optimize find

    -   After Find(x), rewire parent pointers directly to root along the
        path X-r (r is X's root)

    -   Hopcroft-Ullman Theorem

        -   With Union by Rank and Path Compression. M union + find
            operations take **O(mlog\*n)** time, where log\*n = the
            number of times you need to apply log to n before the result
            is \<= 1. E.g. log\* 2\^65536 = 5

        -   I haven't walk through the proof myself yet.

        -   Not optimal yet

    -   Ackerman Function

        -   Tarjar's Bound

> With union by rank and path compression, m union + find operations
> take **O(mα(n)),** where α(n) is the inverse Ackerman Function that's
> even much smaller than log\*n

-   Pros & Cons after Optimize

    -   Union() reduces to two Find()

    -   Find() and Union() worse case takes O(logn)


## Applications
- Lazy Union [code](https://github.com/hzhaoc/utils/blob/main/algo/union_find.py)
- [Clustering problem, function C3W2_2](https://github.com/hzhaoc/utils/blob/main/algo/HW.py)
