'''Crudely joins multiple tables together.'''
import sys
import itertools

import table

def join(tables, name=None):
  if name is None:
    name = "_".join([table.filename for table in tables])
  joined = Table(name, [fieldname for table in tables
    for fieldname in table.fieldnames])
  for row in itertools.izip(*tables):
    joined.append([item for piece in row for item in piece])
  return joined

if __name__ == '__main__':
  if len(sys.argv) >= 3:
    join([table.Table(csv) for csv in sys.argv[1:]])
    print "Success!"
