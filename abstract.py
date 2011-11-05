"""A collection of abstract data types."""
from collections import Counter as multiset


class queue(object):
  def __init__(self):
    self.head = None
    self._last = None
    self._successors = {}

  @property
  def empty(self):
    return self.head is None

  def push(self, item):
    """Append an item to the end of the queue."""
    if self.empty:
      self.head = item
    else:
      self._successors[self._last] = item
    self._last = item

  def pop(self):
    """Return and remove the item in the front of the queue."""
    assert not self.empty, "pop from empty queue"
    popped = self.head
    try:
      self.head = self._successors.pop(self.head)
    except KeyError:
      self.head = None
      self._last = None
    return popped

  def remove(self, item):
    """Remove an item from the queue. Raises a ValueError if item is not in queue."""
    assert item in self._successors or item == self._last, ValueError("item not in queue")
    if self.head == item:
      self.pop()
    else:
      predecessor = self.head
      while self._successors[predecessor] != item:
        predecessor = self._successors[predecessor]
      if self._last == item:
        del self._successors[predecessor]
        self._last = predecessor
      else:
        self._successors[predecessor] = self._successors.pop(item)

  def __len__(self):
    return len(self._successors) + (not self.empty)

  def __iter__(self):
    while not self.empty:
      yield self.pop()


class stack(object):
  '''A stack object, supporting push and pop implementations.'''

  def __init__(self):
    self.head = None
    self._predecessors = {}

  @property
  def empty(self):
    return self.head is None

  def push(self, item):
    '''S.push(object) -- push object on top.'''
    self._predecessors[item], self.head = self.head, item 

  def pop(self):
    '''
    S.pop() -> item -- remove and return top item.
    Raised IndexError if stack is empty.
    '''
    assert not self.empty, "pop from empty queue"
    popped = self.head
    self.head = self._predecessors.pop(self.head)
    return popped
  
  def __len__(self):
    return len(self._predecessors)

  def __iter__(self):
    while not self.empty:
      yield self.pop()
