"""A an algorithm for solving the longest increasing subsequence problem."""
from bisect import bisect_right

def longest(sequence):
    '''Find the longest increasing subsequence with a sequence.'''
    m = [sequence.next()]
    append = m.append
    def foo(num):
        try:
            m[bisect_right(m, num)] = num
            return 0
        except IndexError:
            append(num)
            return 1
    return sum(map(foo, sequence)) + 1
