
def subsets(container):
  subsets = set()
  for e in container:
    x = frozenset(e)
    subsets.add(x)
    new_subsets = set(x | subset for subset in subsets)
    subsets.update(new_subsets)
  return subsets
