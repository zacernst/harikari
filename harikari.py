"""This is a decorator that randomly causes its decorated function to
   throw an exception. You can specify the probablility that the
   exception gets thrown, and you can also specify a list of possible
   exceptions, among which one will be randomly selected.

   This may seem perverse, but it's been handy for testing, especially
   for testing multiprocessing scripts that need to recover from
   weird process hangs.
"""
import random
import functools

def harikari(activate=True,
             exception_list=(Exception,),
             prob=.1):
    """Randomly causes an Exception. Why? For testing.

    :param activate: Activate the decorator if True
    :type activate: ``bool``
    :param exception_list: The exceptions we can throw.
    :type exception_list: ``list`` of ``Exception``
    :param prob: Probability that an exception will be thrown.
    :type prob: ``float``
    """
    def decorator(test_func):
        @functools.wraps(test_func)
        def wrapper(*args, **kwargs):
            if activate:
                if random.random() < prob:
                    some_exception = random.choice(exception_list)
                    raise some_exception
            return test_func(*args, **kwargs)
        return wrapper
    return decorator
