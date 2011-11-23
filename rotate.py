

def rotate(grid, n):
  """Rotates a grid (a list of lists) 90 degrees n times.
  >>> grid = [ \
      [1, 2, 3], \
      [4, 5, 6], \
      [7, 8, 9]]
  >>> rotate(grid, 1)
  [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
  >>> rotate(grid, 2)
  [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
  >>> rotate(grid, 3)
  [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
  >>> rotate(grid, 4)
  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  >>> rotate(grid, -1)
  [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
  """
  i = n % 4
  if i == 0:
    return grid
  elif i == 1:
    return [list(col)[::-1] for col in zip(*grid)]
  elif i == 2:
    return [row[::-1] for row in reversed(grid)]
  elif i == 3:
    return [list(col) for col in reversed(zip(*grid))]
  return grid


if __name__ == "__main__":
  import doctest
  doctest.testmod()
