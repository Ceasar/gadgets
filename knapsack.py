from itertools import product

from space import Space


def knapsack(items, limit):
  """Find the most valuable combination of items given the limit.

  >>> items = set([('green', 12, 4), ('grey', 1, 2), ('blue', 2, 2), ('orange', 1, 1), ('yellow', 4, 10)])
  >>> knapsack(items, 15)
  [('grey', 1, 2), ('yellow', 4, 10), ('orange', 1, 1), ('blue', 2, 2)]
  """
  row = [0] * (limit + 1)
  item_row = [[]] * (limit + 1)
  for name, wt, val in items:
    for w in xrange(limit, wt, -1):
      score = val + row[w-wt]
      if score > row[w]:
        row[w] = score
        item_row[w] = [(name, wt, val)] + item_row[w-wt]
  return item_row[-1]


def build_spaces(limits):
  '''Builds the vspace and ispace.'''
  #Need to adjust to allow for 0-d
  adjusted = [l + 1 for l in limits]
  return Space(adjusted, int), Space(adjusted, list)


def nknapsack(items, limits):
  """Find the most valuable combination of items given the limit.

  >>> items = set([('green', 12, 8, 4), ('grey', 1, 2, 1), ('blue', 2, 3, 2), ('orange', 1, 5, 2), ('yellow', 4, 6, 10)])
  >>> nknapsack(items, (10, 20))
  [('grey', 1, 2, 1), ('orange', 1, 5, 2), ('blue', 2, 3, 2), ('yellow', 4, 6, 10)]
  """
  vspace, ispace = build_spaces(limits)
  for item in items:
    constraints, val = item[1:-1], item[-1]
    #we reverse-sort here in order to ensure that we don't get
    #duplicate items. if we didn't, ispace[remaining] could
    #contain a copy of the item
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


if __name__ == "__main__":
	import doctest
	doctest.testmod()
