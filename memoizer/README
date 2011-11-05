A simple memoizer class. Allows for creation of modular strategies. 

Using the memoizer is simple. Simply decorate a function with an instantiated Memoizer using a
strategy of choice.


EXAMPLE USAGE:

@Memoizer(strategy=Perfect()) #recalls everything perfectly
def fib(x):
  if x < 2:
    return 1
  else:
    return fib(x-1) + fib(x-2)


@Memoizer(strategy=MRU(maxsize=10)) #recalls the last ten values
def fib(x):
  if x < 2:
    return 1
  else:
    return fib(x-1) + fib(x-2)


STRATEGIES:

It's often inefficient to memoize a function with perfect recall. That's where strategies come
in. Strategies lets you define how you want remember things.

EXAMPLE STRATEGIES:

#strategies/perfect.py
import functools
import cPickle

class Perfect(object):
  """A naive memoization strategy. Remembers everything."""
  def __call__(self, func):
    cache = {}
    @functools.wraps(func)
    def memoized(*args, **kwargs):
      hash_ = cPickle.dumps((args, set(kwargs.iteritems())))
      try:
        return cache[hash_]
      except KeyError:
        cache[hash_] = func(*args, **kwargs)
        return cache[hash_]
    return memoized


#strategies/mru.py
import functools
import cPickle

class MRU(object):
  """A short-term memoization strategy. Remembers the most recently used values.
  
  If no maxsize is specified, the strategy stores at the most 10."""
  def __init__(self, maxsize=10):
    self.maxsize = maxsize

  def __call__(self, func):
    cache = {}
    queue = [] #a list of keys
    @functools.wraps(func)
    def memoized(*args, **kwargs):
      hash_ = cPickle.dumps((args, set(kwargs.iteritems())))
      try:
        result = cache[hash_]
      except KeyError:
        result = func(*args, **kwargs)
        if len(queue) > self.maxsize:
          del cache[queue.pop(0)]
        cache[hash_] = result
        queue.append(hash_)
      else:
        queue.remove(hash_)
        queue.append(hash_)
      return cache[hash_]
    return memoized

