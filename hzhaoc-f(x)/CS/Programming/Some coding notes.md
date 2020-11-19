### notes

1.  a is b vs. id(a) == id(b), where a and b are classes

    1.  In 'a is b' logic expression, both sides of the logic
        expressions are classes.

        1.  First, both classes are initialized at the same time and
            allocated to two different memory spaces.

        2.  Then the logic expression evaluates **False.**

        3.  Then both class instances are deleted.

    2.  In 'id(a) == id(b)' logic expression, both sides are functions.

> 1.2.1. First a new class a is initialized and passed to left function.
>
> 1.2.2. Next the address of the memory for that new class instance is
> returned.
>
> 1.2.3. Next the new class instance is deleted.
>
> 1.2.4. Next a new class b is initialized and passed to right function
>
> 1.2.5. Next runs the id() function, returns the address of the memory
> for that new class instance b
>
> 1.2.6. New class instance b is deleted.
>
> 1.2.6. Next evaluate the == logic expressions to be **True.**

2.  Generator vs iterator

> Generator can only be traversed once and will be deleted
>
> Iterator won't be deleted when traversed.

3.  Generator expression execution time order

> \>\>\> array = \[1, 8, 15\]
>
> \>\>\> g = (x for x in array if array.count(x) \> 0)
>
> \>\>\> array = \[2, 8, 22\]
>
> \>\>\> print(list(g))
>
> \[8\]
>
> \>\>\> array = \[1, 8, 15\]
>
> \>\>\> g = (x for x in array if x \> 20)
>
> \>\>\> array = \[2, 8, 22\]
>
> \>\>\> print(list(g))
>
> \[\]
>
> I guess generator statement is evaluated at compile time, the count
> method in the if statement is evaluated at runtime To start
> with, at compile time, generator go through the array \[1, 8, 15\],
> and then array points to new object \[2, 8, 22\]. Then in runtime, the
> count method in if statement is evaluated where the new object that
> array points to: \[1, 8, 15\] is passed to that method.
>
> \>\>\> array_1 = \[1,2,3,4\]
>
> \>\>\> g1 = (x for x in array_1)
>
> \>\>\> array_1 = \[1,2,3,4,5\]
>
> \>\>\> array_2 = \[1,2,3,4\]
>
> \>\>\> g2 = (x for x in array_2)
>
> \>\>\> array_2\[:\] = \[1,2,3,4,5\]
>
> \>\>\> print(list(g1))
>
> \[1,2,3,4\]
>
> \>\>\> print(list(g2))
>
> \[1,2,3,4,5\]
>
> This output difference is due to ways of assigning values to
> variables. In the first situation, \[1, 2, 3, 4, 5\] is a new object
> that arrary_1 variable point at, the old object \[1, 2, 3, 4\] is
> deleted in memory. In the second situation, \[1, 2, 3, 4, 5\] is
> modified from \[1, 2, 3, 4\] by list slicing so array_2 points to the
> same but modified object.

4.  Immutable vs mutable objects

5.  Closure

> When a nested function invokes a variable outside its scope but still
> not a global variable
>
> (from the enclosing function), it is called a closure.
>
> Usages: Closures can avoid global variables, its referenced/invoked
> variable outside its scope can be tracked and won't be deleted from
> memory when the closure function is in execution.
>
> Circumstances to use closures: Web crawling, decorator

6.  Decorator

> \@decorator
>
> def func():
>
> pass
>
> A syntax sugar for decorator function (it is a closure) to wrap up a
> function. The decorator itself is a closure function which is a
> function object that remembers values in its enclosing scope, even if
> they are not present in memory. It helps a function to add additional
> functions without editing the function itself.
>
> If there are multiple uncertain parameters to pass to func(), use
> \*args, and \*\*kwargs to unpack, making parameter passing dynamic;
>
> Decorator can be nested; (multi-layered)
>
> A function can have multiple decorators;
>
> Circumstances to use decorators: log, test efficiency, cache

7.  \_\_name\_\_, \_\_doc\_\_ attribute of function object

> \_\_name\_\_: function name
>
> \_\_doc\_\_: texts in """xxx"""
>
> In a decorator, if warps module is added, \_\_doc\_\_, \_\_name\_\_,
> will be changed to the attribute of the decorated function.
>
> from functools import wraps
>
> def wrapper(f):
>
> \@wraps(f)
>
> def inner(\*args, \*\*kwargs):
>
> \'\'\'before function\'\'\'
>
> ret = f(\*args,\*\*kwargs)
>
> \'\'\'after function\'\'\'
>
> return ret
>
> return inner
>
> \@wrapper
>
> def func1():
>
> \"\"\"
>
> This function is used to log in
>
> return: log is successful of not（True，False）
>
> \"\"\"
>
> print(666)
>
> return True
>
> func1()
>
> print(func1.\_\_name\_\_)
>
> print(func1.\_\_doc\_\_)

8.  Map, Filter, Reduce

    1.  Map

> Map function applies a function with passed arguments given by an
> iterator. It returns a generator object within which are a 'list' of
> that function returns.

2.  Filter

> Filter function applies a function with passed arguments given by an
> iterator. It returns a generator object within which are a 'list' of
> elements in iterator when the function which the elements passed to
> returns true.

3.  Reduce

> Reduce function applies a function with passed arguments given by a
> sequential. It first passes the first two elements in the sequential
> to the arguments and attain the return result. Then it iterates
> through the remaining elements in the sequential, passing the element
> and last return result to the function, keeping the new returns as the
> new result in every iteration until it traversed all elements in the
> sequential.
>
> Reduce is a module from **functools**.

9.  Regular Expression

> Greedy/non-greedy, special sequence, escape characters, sets, captures

