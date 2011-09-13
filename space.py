from itertools import product

from vector import Vector

class Matrix(list):
  '''A null matrix of specified dimensions.

  >>> m = Matrix((2, 2))
  >>> m
  [[0, 0], [0, 0]]
  >>> m[0][1]
  0
  >>> m = Matrix((2, 2, 2), 1)
  >>> m
  [[[1, 1], [1, 1]], [[1, 1], [1, 1]]]
  >>> m[0][1][0]
  1
  '''
  def __init__(self, dimensions, default=0):
    print dimensions
    if len(dimensions) > 1:
      super(Matrix, self).__init__([Matrix(dimensions[1:], default)
        for d in xrange(dimensions[0])])
    else:
      super(Matrix, self).__init__([default] * dimensions[0])

class Space(dict):
  '''A null space of specified dimensions.

  >>> s= Space((2, 2))
  >>> s
  {(0, 1): 0, (1, 0): 0, (0, 0): 0, (1, 1): 0}
  >>> s = Space((2, 2, 2), [])
  >>> s
  {(0, 1, 1): [], (1, 1, 0): [], (1, 0, 0): [], (0, 0, 1): [], (1, 0, 1): [], (0, 0, 0): [], (0, 1, 0): [], (1, 1, 1): []}
  '''
  def __init__(self, dimensions, default=0):
    for point in product(*[range(d) for d in dimensions]):
      self[Vector(point)] = default
