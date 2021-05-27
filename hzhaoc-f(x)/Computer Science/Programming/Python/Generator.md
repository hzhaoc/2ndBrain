From [realpython.com](https://realpython.com/introduction-to-python-generators/):

> Introduced with PEP 255, generator functions are a special kind of function that return a lazy iterator. These are objects that you can loop over like a list. However, unlike lists, lazy iterators do not store their contents in memory.

Generator is iterated for one-time use. Examples with its methods `send()`, `close()`, `throw()` are in [realpython.com](https://realpython.com/introduction-to-python-generators/).

### Yield expressions
New in Python 2.5. According to [docs.python.org](https://docs.python.org/release/2.7/reference/expressions.html#yield-expressions):

> The yield expression is only used when defining a generator function, and can only be used in the body of a function definition. Using a yield expression in a function definition is sufficient to cause that definition to create a generator function instead of a normal function.

For more details, go to [docs.python.org](https://docs.python.org/release/2.7/reference/expressions.html#yield-expressions)