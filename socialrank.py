"""Mapper class"""
from __future__ import division
from collections import defaultdict


def rank(g, accept=1e-3):
  """Performs an iterative algorithm on a graph to assess the influence of each node.
  
  >>> edges = set([(1, 2), (1, 3), (2, 4), (3, 1), (3, 4), (3, 5), (5, 1), (5, 4)]) 
  >>> g = (set(xrange(1, 6)), edges)
  >>> rank(g)
  [(4, 0.5789168557971544), (1, 0.3313874448771381), (2, 0.2909555159840314), (3, 0.2909555159840314), (5, 0.2325098036400054)]
  """
  d = 0.15
  vertices, edges = g

  def B(i):
    '''Generate i's fans.'''
    assert i in vertices, "%s not in vertices(%s)" % (i, vertices)
    for edge in edges:
      if edge[1] == i:
        yield edge[0]

  def N(i):
    '''Generate i's idols.'''
    assert i in vertices, "%s not in vertices(%s)" % (i, vertices)
    for edge in edges:
      if edge[0] == i:
        yield edge[1]
    
  r = defaultdict(dict, {0: dict((v, 1) for v in vertices)})
  k = 0
  while True:
    for v in vertices:
      r[k+1][v] = d + (1 - d) * sum(1 / len(set(N(j))) * r[k][j] for j in B(v))
    k += 1
    if all(abs(r[k][v] - r[k-1][v]) < accept for v in vertices):
      break
  return sorted(r[k].items(), reverse=True, key=lambda p: p[1])

if __name__ == "__main__":
  import doctest
  doctest.testmod()
