'''Contains the base memoizer object.'''


class Memoizer(object):
  """
  A memoizer object.

  Takes a strategy and applies it to a function.
  """
  def __init__(self, strategy):
    self.strategy = strategy

  def __call__(self, func):
    return self.strategy(func)

"""
def memoize(strategy):
  def wrap(func):
    return strategy(func)
  return wrap
"""
