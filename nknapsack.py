from itertools import product

from space import Space

def nknapsack(items, limits):
  """Find the most valuable combination of items given the limit.

  >>> items = set([('green', 12, 8, 4), ('grey', 1, 2, 1), ('blue', 2, 3, 2), ('orange', 1, 5, 2), ('yellow', 4, 6, 10)])
  >>> nknapsack(items, (10, 20))
  [('orange', 1, 5, 2), ('yellow', 4, 6, 10), ('grey', 1, 2, 2), ('blue', 2, 3, 2)]
  """
  #Need to adjust to allow for 0-d
  adjusted = [l + 1 for l in limits]
  vspace = Space(adjusted, 0)
  ispace = Space(adjusted, [])
  for item in items:
    name, val = item[0], item[-1]
    constraints = item[1:-1]
    #we reverse-sort here in order to ensure that we don't get
    #duplicate items
    for vpoint in sorted(vspace, reverse=True):
      #make sure we don't get a negative point, not in the space
      if all([v >= c for v, c in zip(vpoint, constraints)]):
        #all point in spaces are actually vectors, allowing us
        #to substract intuitively here
        remaining = vpoint - constraints
        score = val + vspace[remaining]
        if score > vspace[vpoint]:
          vspace[vpoint] = score
          ispace[vpoint] = [item] + ispace[remaining]

  return ispace[limits]


