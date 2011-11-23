"""
A collection of data structures that emulate a hierarchal tree structure
with a set of linked nodes.
"""
import heapq
    

#TODO: add a __contains__ method if possible, or just use a sorted list with bisect
class heap(object):
    '''A tree-based data structure that satisfies the heap property.

    A heap can be used as priority queue by pushing tuples onto the heap.
    '''
    def __init__(self, items):
        self._items = list(items)
        heapq.heapify(self._items)

    @property
    def top(self):
        return self._items[0]

    @property
    def empty(self):
        return len(self) == 0

    def pop(self):
        '''Pop and return the smallest item from the heap, maintaining the heap
        invariant. If the heap is empty, IndexError is raised.
        '''
        try:
          return heapq.heappop(self._items)
        except IndexError as e:
          raise e

    def push(self, item):
        '''Push the value item onto the heap, maintaining the heap invariant.
        If the item is not hashable, a TypeError is raised.
        '''
        try:
          hash(item)
        except TypeError as e:
          raise e
        else:
          heapq.heappush(self._items, item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        while len(self) > 0:
            yield self.pop()


class RecursiveDict(dict):
    '''
    A recursive defaultdict.

    >>> a = RecursiveDict()
    >>> a[1][2][3] = 4
    >>> dict(a)
    {1: {2: {3: 4}}}
    '''
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value
