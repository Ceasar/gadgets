"""A generator wrapper used to force the generate to produce only unique values."""

def sieve(gen):
  """Wraps a generator. Forces the generates to produce only unique values.

  >>> import random
  >>> @sieve
  ... def randbinstream(x):
  ...   for r in xrange(x):
  ...     yield random.randint(0, 1) 
  >>> print len([i for i in randbinstream(10)]) <= 2
  True
      
  """
  items = set()
  def wrap(*args, **kwargs):
    for item in gen(*args, **kwargs):
      if item not in items:
      	yield item
      	items.add(item)
  return wrap

if __name__ == "__main__":
  import doctest
  doctest.testmod()
