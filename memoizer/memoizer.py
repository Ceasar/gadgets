'''Contains the base memoizer object.'''


class Memoizer(object):
  """A memoizer object. Speeds up functions at the cost of memory.

  If no strategy is provided the memoizer will remember everything.
  """
  def __init__(self, strategy=None):
    self.strategy = strategy

  def __call__(self, func):
    return self.strategy(func)
