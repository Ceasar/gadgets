'''A module for counting operations.'''
from __future__ import division

import copy
import itertools
import operator

from collections import defaultdict
from math import factorial


def product(nums):
  return reduce(operator.mul, nums)

def permutation(n, k):
    '''Get the permutation of n choose k objects.'''
    return factorial(n) / factorial(n - k)

def combination(n, k):
    '''Get the combination of n choose k objects.'''
    return permutation(n, k) / factorial(k)

def arrange(n, ordered=True, *k):
  if sum(k) != n:
    raise ValueError("n must equal sum(k)!")
  if ordered:
    return factorial(n) / product(k)
  else:
    return factorial(n) / product(k) / factorial(len(k))

class Multiset(defaultdict):
  '''A set which keeps track of the number of items inserted.'''
  def __init__(self, items=None):
    if items is None:
      super(Multiset, self).__init__(int)
    else: 
      super(Multiset, self).__init__(int, items)

  @property
  def cardinality(self):
    return sum(self.values())

  def coefficient(self, k):
    return combination(self.cardinality, k)

  def draw(self, items, replacement=True):
    p = 1.0
    if replacement:
      for item, multiplicity in items.iteritems():
        p *= (self[item] / self.cardinality) ** multiplicity
    else:
      for item, multiplicity in items.iteritems():
        p *= combination(self[item], multiplicity)
      p /= self.coefficient(sum(items.values()))
    return p


