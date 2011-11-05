def divide(n, k):
  '''Divide n into sets of size of k or smaller.

  Returns a generator.

  >>> items = range(12)
  >>> for piece in divide(items, 4): print piece
  [0, 1, 2, 3]
  [4, 5, 6, 7]
  [8, 9, 10, 11]
  '''
  for i in range(0, len(n), k):
    yield n[i:i+k]


if __name__ == "__main__":
	import doctest
	doctest.testmod()
