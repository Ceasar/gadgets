'''
Simple mapreduce function.

Example Use
===========

def init(in1):
  """Read the file in the input dir, convert the values into the intermediate
  format, and output the data to the output directory."""
  def mapper(edge):
    return edge[0], edge[1]
  def reducer(key, vals):
    return {'node': key, 'rank': 1, 'idols': (val for val in vals)}
  return mapreduce(mapper, reducer, in1)
'''
from itertools import groupby


def mapreduce(mapper, reducer, *inputs):
  sorter = lambda x: x[0]
  return map(reducer, groupby(map(mapper, *inputs), sorter))
