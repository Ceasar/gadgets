"""A queue object, implemented using native types."""


class queue(object):
  def __init__(self):
    self.head = None
    self.last = None
    self.successors = {}

  @property
  def empty(self):
    return self.head is None

  def push(self, item):
    """Append an item to the end of the queue."""
    if self.empty:
      self.head = item
    else:
      self.successors[self.last] = item
    self.last = item

  def pop(self):
    """Return and remove the item in the front of the queue."""
    assert not self.empty, "pop from empty queue"
    popped = self.head
    try:
      self.head = self.successors.pop(self.head)
    except KeyError:
      self.head = None
      self.last = None
    return popped


def _test():
  q = queue()
  q.push(0)
  q.push(1)
  q.push(3)
  print q.head, q.last, q.successors
  assert q.pop() == 0
  print q.head, q.last, q.successors
  assert q.pop() == 1
  print q.head, q.last, q.successors
  assert q.pop() == 3
  print q.head, q.last, q.successors
  print "success"


if __name__ == "__main__":
  _test()
