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
    '''Q.push(object) -- push object on back of queue.'''
    if self.empty:
      self.head = item
    else:
      self._successors[self._last] = item
    self._last = item

  def pop(self):
    '''
    Q.pop() -> item -- remove and return first item.
    Raises IndexError if queue is empty.
    '''
    assert not self.empty, IndexError("pop from empty queue")
    popped = self.head
    try:
      self.head = self._successors.pop(self.head)
    except KeyError:
      self.head = None
      self._last = None
    return popped

  def remove(self, item):
    """Q.remove(value) -- remove first occurence of value.
    Raises a ValueError if item is not present."""
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
    Raises IndexError if stack is empty.
    '''
    assert not self.empty, IndexError("pop from empty queue")
    popped = self.head
    self.head = self._predecessors.pop(self.head)
    return popped
  
  def __len__(self):
    return len(self._predecessors)

  def __iter__(self):
    while not self.empty:
      yield self.pop()
