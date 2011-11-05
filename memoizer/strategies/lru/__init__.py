import functools
import cPickle

from queue import queue


class LRU(object):
  """A short-term memoization strategy. Evicts old values.

  If no maxsize is specified, the strategy stores at the most 10."""
  def __init__(self, maxsize=10):
    self.maxsize = maxsize

  def __call__(self, func):
    cache = {}
    q = queue()  # a list of keys

    @functools.wraps(func)
    def memoized(*args, **kwargs):
      hash_ = cPickle.dumps((args, set(kwargs.iteritems())))
      try:
        result = cache[hash_]
      except KeyError:
        result = func(*args, **kwargs)
        if len(q) > self.maxsize:
          del cache[q.pop()]
        cache[hash_] = result
      else:
        q.remove(hash_)
      finally:
        q.push(hash_)
      return cache[hash_]
    return memoized
