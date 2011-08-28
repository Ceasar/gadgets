'''A stack object, supporting push and pop implementations.

Implemented using a linked list. Technically, not neccesarry since Python's list
supports pop and append, but marking a list as a stack can be linguistically
simpler, especially when iterating.'''

class _Element(object):
    def __init__(self, object, next):
        self.object = object
        self.next = next

class stack(object):
    '''A stack object, supporting push and pop implementations.'''

    @property
    def empty(self):
        return self._head == None
    
    def __init__(self, iterable=None):
        self._head = None
        try:
            iterable = list(iterable)
        except:
            pass
        else:
            while iterable:
                self.push(iterable.pop(0))
    
    def push(self, object):
        '''S.push(object) -- push object on top.'''
        self._head = _Element(object, self._head)

    def peek(self):
        '''
        S.peek() -> item -- return top item.
        Raises IndexError if stack is empty.
        '''
        if self.empty: raise IndexError('peek at empty list')
        return self._head.object

    def pop(self):
        '''
        S.pop() -> item -- remove and return top item.
        Raised IndexError if stack is empty.
        '''
        if self.empty: raise IndexError('pop from empty list')
        object = self._head.object
        self._head = self._head.next
        return object

    def __iter__(self):
        while not self.empty:
            yield self.pop()
