
class Arc(tuple):
  def __init__(self, iterable):
    assert len(iterable) == 2, ValueError('tuple must be length 2')
    super(Arc, self).__init__(iterable)

  @property
  def tail(self):
    return self[0]

  @property
  def head(self):
    return self[1]

  @property
  def inverted(self):
    return (self.head, self.tail)


class Digraph(object):
  def __init__(self):
    self.nodes = set()
    #an edge is an ordered pair (i, j) representing a link from node i to node j.
    self.arcs = set() #set of tuples

  @property
  def symmetric(self):
    for arc in self.arcs:
      if arc.inverted not in self.arcs:
        return False
    return True

  @property
  def oriented(self):
    for arc in arcs:
      if arc.inverted in self.arcs:
        return False
    return True

  def outcoming(self, node):
    for arc in self.arcs:
      if arc.tail == node:
        yield arc
  
  def outdegree(self, node):
    return len([arc for arc in outcoming(node)])

  def incoming(self, node):
    for arc in self.arcs:
      if arc.head == node:
        yield arc

  def indegree(self, node):
    return len([arc for arc in incoming(node)])

  def source(self, node):
    return indegree(node) == 0

  @property
  def balanced(self):
    return all([self.indegree(node) == self.outdegree(node) for node in self.nodes])
