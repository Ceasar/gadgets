from listtools import divide

EXPECTED = set(xrange(1, 10))

def sudoku(grid):
  """Checks if a grid is solved correctly.
  A grid should be a matrix (a list of lists.)
  >>> grid = [ \
      [1, 2, 3, 4, 5, 6, 7, 8, 9], \
      [4, 5, 6, 7, 8, 9, 1, 2, 3], \
      [7, 8, 9, 1, 2, 3, 4, 5, 6], \
      [2, 3, 4, 5, 6, 7, 8, 9, 1], \
      [5, 6, 7, 8, 9, 1, 2, 3, 4], \
      [8, 9, 1, 2, 3, 4, 5, 6, 7], \
      [3, 4, 5, 6, 7, 8, 9, 1, 2], \
      [6, 7, 8, 9, 1, 2, 3, 4, 5], \
      [9, 1, 2, 3, 4, 5, 6, 7, 8]]
  >>> sudoku(grid)
  True
  >>> grid = [ \
      [9, 1, 2, 3, 4, 5, 6, 7, 8], \
      [1, 2, 3, 4, 5, 6, 7, 8, 9], \
      [4, 5, 6, 7, 8, 9, 1, 2, 3], \
      [7, 8, 9, 1, 2, 3, 4, 5, 6], \
      [2, 3, 4, 5, 6, 7, 8, 9, 1], \
      [5, 6, 7, 8, 9, 1, 2, 3, 4], \
      [8, 9, 1, 2, 3, 4, 5, 6, 7], \
      [3, 4, 5, 6, 7, 8, 9, 1, 2], \
      [6, 7, 8, 9, 1, 2, 3, 4, 5]]
  >>> sudoku(grid)
  False
  """
  for row in grid:
    assert len(row) == 9
    if set(row) != EXPECTED:
      return False
  for col in zip(*grid):
    assert len(col) == 9
    if set(col) != EXPECTED:
      return False
  for rect in divide(grid, 3):
    for square in divide(zip(*rect), 3):
      if set(i for col in square for i in col) != EXPECTED:
        return False
  return True

if __name__ == '__main__':
  import doctest
  doctest.testmod()
