'''
A specialized tree-based data structure that satisfies the heap property.

A heap can be used as priority queue by pushing tuples onto the heap.
'''

import heapq
    

class heap(object):
    '''A specialized data structure that satisfies the heap property.'''
    def __init__(self, iterable=None):
        if iterable is None:
            self._heap = []
        else:
            self._heap = list(iterable)
        heapq.heapify(self._heap)

    def _immutable(self, func, *args):
        '''Checks if the argument is immutable in order to ensure integrity
        of the heap. Raises TypeError if the argument is mutable.

        Note that there is no way to ensure an object is in fact immutable
        in Python. This function checks if the arguments are hashable and
        assumes that the arguments behave nicely.'''
        try:
            hash(args[-1])
        except TypeError as e:
            raise e
        else:
            func(*args)

    def pop(self):
        '''
        Pop and return the smallest item from the heap, maintaining the heap
        invariant. If the heap is empty, IndexError is raised.
        '''
        return heapq.heappop(self._heap)

    def push(self, item):
        '''
        Push the value item onto the heap, maintaining the heap invariant.
        '''
        return self._immutable(heapq.heappush, self._heap, item)

    def pushpop(self, item):
        '''
        Push item on the heap, then pop and return the smallest item from
        the heap.

        The combined actions runs more efficiently than heappush()
        followed by a separate called to heappop().'''
        return self._immutable(heapq.heappushpop, self._heap, item)

    def poppush(self, item):
        '''
        Pop and return the smallest item from the heap, then push item on
        the heap.

        The combined actions runs more efficiently than heappop()
        followed by a separate called to heappush().'''
        return self._immutable(heapq.heapreplace, self._heap, item)

    def __setitem__(self, i, y):
        def setitem(i, y):
            self._heap[self._heap.index(i)] = y
            heapq.heapify(self._heap)
        self._immutable(setitem, i, y)

    def __len__(self):
        return len(self._heap)

    def __iter__(self):
        while self._heap:
            yield self.pop()

