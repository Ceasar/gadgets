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

  def remove(self, item):
    """Remove an item from the queue. Raises a ValueError if item is not in queue."""
    assert item in self.successors or item == self.last, ValueError("item not in queue")
    if self.head == item:
      self.pop()
    else:
      predecessor = self.head
      while self.successors[predecessor] != item:
        predecessor = self.successors[predecessor]
      if self.last == item:
        del self.successors[predecessor]
        self.last = predecessor
      else:
        self.successors[predecessor] = self.successors.pop(item)

  def __len__(self):
    return len(self.successors) + (not self.empty)


def _test():
  q = queue()
  q.push(0)
  q.push(1)
  q.push(3)
  assert q.pop() == 0
  assert q.pop() == 1
  assert q.pop() == 3

  q.push(2)
  q.push(4)
  q.remove(2)
  assert q.pop() == 4

  q.push(2)
  q.push(4)
  q.remove(4)
  q.push(6)
  assert q.pop() == 2
  assert q.pop() == 6

  q.push(2)
  q.push(4)
  q.push(5)
  q.remove(4)
  assert q.pop() == 2
  assert q.pop() == 5

  print "success"


if __name__ == "__main__":
  _test()
