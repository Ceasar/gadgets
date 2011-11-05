'''A recursive defaultdict.

Essentially, an implementation of perl's autovivification feature.'''

class RecursiveDict(dict):
    '''A recursive defaultdict.

    >>> a = RecursiveDict()
    >>> a[1][2][3] = 4
    >>> dict(a)
    {1: {2: {3: 4}}}
    '''
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value
