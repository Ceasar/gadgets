"""A collection of functions for manipulating iterables."""

flatten = lambda *x: sum(x, [])

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


if __name__ == "__main__":
	import doctest
	doctest.testmod()
