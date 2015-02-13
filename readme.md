Harikari
========

This script contains a decorator, called `harikari`. When you decorate
a function with `harikari`, that function will randomly throw an
exception with a given probability. You can optionally specify a
tuple of exceptions from which one will be randomly selected. You can
also specify the probability of the function throwing an exception.

This has been useful for testing scripts that have to operate under
unpredictable circumstances. For example, I have used it to test
multiprocessing scripts that have to interface with external data
sources that are unreliable, or may return bad data.

In the future, I'll add the ability to specify a probability that the
exception is thrown within a specified time period -- for instance,
to specify that there is a 10% chance of throwing an exception each
minute.

Usage
-----

Just import `harikari.harikari` and wrap your function with it:

```
from harikari import harikari

@harikari()
def my_great_function(some_argument):
    do_something()
    return something
```

You can specify optional arguments, like so:
```
@harikari(activate=True, prob=.01,
          exception_list=(TypeError, KeyError,))
```
In this case, the probability of throwing an exception is 1%, the
exception thrown will be either TypeError or KeyError. You can
set the `activate` argument to False if you want to disable the
decorator.

By default, `activate=True`, `prob=.1`, and `exception_list=(Exception,)`.

