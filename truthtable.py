import inspect
import itertools

def truthtable(func):
  """Build a truthtable for a function.

  The function should only take booleans and return booleans."""
  args = inspect.getargspec(func).args
  table = {}
  for inputs in itertools.product(*[(0, 1) for arg in args]):
    table[inputs] = func(*inputs)
  return table

def NOT(a):
  return not a

def AND(a, b):
  return a and b

def NAND(a, b):
  return NOT(AND(a, b))

def OR(a, b):
  return a or b

def NOR(a, b):
  return NOT(OR(a, b))

def XOR(a, b):
  return a != b

def XNOR(a, b):
  return a == b
