"""A collection of functions for manipulating iterables."""
from itertools import izip


#NOTE: Generally itertools.chain is a better solution than either of the below
flatten = lambda *x: sum(x, [])
splice = lambda x, i, y: x[:i] + y + x[i:] 


def divide(list_, k):
  '''Slice a list into pieces of length-k.

  >>> items = range(12)
  >>> for piece in divide(items, 4): print piece
  [0, 1, 2, 3]
  [4, 5, 6, 7]
  [8, 9, 10, 11]
  '''
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
