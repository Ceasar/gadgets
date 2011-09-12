

class Space(list):
  '''A null matrix of specified dimensions.

  s = Space(2, 2)
  >>> s
  [[0, 0], [0, 0]]
  >>> s[0][1]
  0
  >>> s = Space(2, 2, 2)
  >>> s
  [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
  >>> s[0][1][0]
  0
  '''
  def __init__(self, *dimensions):
    if len(dimensions) > 1:
      super(Space, self).__init__([Space(*dimensions[1:]) for d
        in xrange(dimensions[0])])
    else:
      super(Space, self).__init__([0] * dimensions[0])
