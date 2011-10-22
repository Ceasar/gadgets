'''A stack cargo, supporting push and pop implementations.

Implemented using a linked list. Technically, not neccesarry since Python's list
supports pop and append, but marking a list as a stack can be linguistically
simpler, especially when iterating.'''


class Node(object):
  def __init__(self, cargo, next_):
    self.cargo = cargo
    self.next_ = next_


class LinkedList(object):
  '''A stack cargo, supporting push and pop implementations.'''

  def __init__(self, head):
    self.head = Node(head, None)

  @property
  def empty(self):
    return self.head is None

  def push(self, cargo):
    '''S.push(cargo) -- push cargo on top.'''
    self.head = Node(cargo, self.head)

  def peek(self):
    '''
    S.peek() -> item -- return top item.
    Raises IndexError if stack is empty.
    '''
    assert not self.empty, 'peek at empty list'
    return self.head.cargo

  def pop(self):
    '''
    S.pop() -> item -- remove and return top item.
    Raised IndexError if stack is empty.
    '''
    assert not self.empty, 'pop from empty list'
    cargo = self.head.cargo
    self.head = self.head.next_
    return cargo

  def reverse(self):
    self.head.next_, current = None, self.head.next_ 
    if current is not None:
      next_, current.next_  = current.next_, self.head
      while next_ is not None:
        next_.next_, current, next_ = current, next_, next_.next_
      self.head = current

  def __iter__(self):
    node = self.head
    while node:
      yield node.cargo
      node = node.next_

  def insert_after(self, lead, cargo):
    for node in self:
      if node.cargo == lead:
        lead.next_ = Node(cargo, lead.next_)
        return True
    return False

  def remove(self, cargo):
    '''L.remove(value) -- remove first occurence of value.
    Raises ValueError if the value is not present.'''
    for node in self:
      if node.next_.cargo == cargo:
        node.next_ = node.next_.next_
        return
    raise ValueError('list.remove(x): x not in list')


