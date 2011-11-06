"A collection of function for enumerating an interable in different ways."
from itertools import izip


def rr_enumerate(iterable):
  '''Enumerate a reversed iterable.'''
  return izip(reversed(xrange(len(iterable))), reversed(iterable))

def fr_enumerate(iterable):
  '''Enumerate a reversed iterable.'''
  return izip(xrange(len(iterable)), reversed(iterable))

def rf_enumerate(iterable):
  '''Enumerate a reversed iterable.'''
  return izip(reversed(xrange(len(iterable))), iterable)
