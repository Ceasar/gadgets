"""A snippet for generating subsets of a set."""

def subsets(set_):
  '''Get each of the subsets for a given set.

  >>> subsets(set((1, 2, 3)))
  set([frozenset([3]), frozenset([1, 2]), frozenset([]), frozenset([2, 3]), frozenset([1]), frozenset([1, 3]), frozenset([1, 2, 3]), frozenset([2])])
  '''
  if len(set_) == 1:
    #return the empty set, and the singleton set
    return set((frozenset(), frozenset(set_))) 
  else:
    #copy the set, so as to not modify the input
    cloned = set_.copy()
    n = frozenset((cloned.pop(),))
    reduced = subsets(cloned)
    return reduced | set([sub | n for sub in reduced.copy()])


if __name__ == "__main__":
	import doctest
	doctest.testmod()
