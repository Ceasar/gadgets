import unittest

from memoizer import Memoizer
from strategies.mru import MRU

"""
So I'm not really sure how to test decorators. Since fib calls fib, if gib=fib and I memoize
gib, fib still calls fib, which means gib only remembers the final outputs, rather than the
steps in-between.
"""

@Memoizer(strategy=MRU(maxsize=10))
def fib(x):
  if x < 2:
    return 1
  else:
    return fib(x-1) + fib(x-2)


class TestMemoizer(unittest.TestCase):
  def setUp(self):
    self.func = Memoizer(fib)

  def test_simple(self):
    self.assertEqual(self.func(0), 1)
    self.assertEqual(self.func(1), 1)
    self.assertEqual(self.func(10), 89)


if __name__ == '__main__':
  unittest.main()
