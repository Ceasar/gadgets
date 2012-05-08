"""A collection of functions for manipulating iterables."""
from itertools import chain, izip, islice


def flatten(*x):
    """Flatten a list of lists.
    >>> lists = [[1, 2], [3, 4], [5, 6]]
    >>> list(flatten(*lists))
    [1, 2, 3, 4, 5, 6]
    """
    return chain(*x)


def splice(x, i, y):
    """Splice one list into another.
    >>> items = [1, 2, 5, 6]
    >>> list(splice(items, 2, [3, 4]))
    [1, 2, 3, 4, 5, 6]
    """
    return chain(islice(x, 0, i), y, islice(x, i, len(x)))


def divide(list_, k):
  """Slice a list into pieces of length-k.
  >>> items = range(1, 7)
  >>> list(divide(items, 2))
  [[1, 2], [3, 4], [5, 6]]
  """
  for i in range(0, len(list_), k):
    yield list_[i:i+k]


def rr_enumerate(iterable):
  '''Enumerate a reversed iterable.'''
  return izip(reversed(xrange(len(iterable))), reversed(iterable))


def fr_enumerate(iterable):
  '''Enumerate a reversed iterable.'''
  return izip(xrange(len(iterable)), reversed(iterable))


def rf_enumerate(iterable):
  '''Enumerate a reversed iterable.'''
  return izip(reversed(xrange(len(iterable))), iterable)


if __name__ == "__main__":
  import doctest
  doctest.testmod()
