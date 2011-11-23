
def probability(set):
  pass #takes a set

def indicator(a):
  return int(bool(a))

def expected(i_a):
  return 1 * p(a) + 0 * p(a_complement) #= p(a)

def conditional(a, b):
  return p(a AND b) / p(b)

def condition2(x, b):
  #a is a random variable and b is a set
  #random variable is a map from a set to the real line
  return expected(indicator(b) * x) / expected(indicator(b))
