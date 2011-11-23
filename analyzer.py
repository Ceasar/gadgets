import sys

from statistics.regression import MultipleRegression

from table import Table

def split(table):
  '''Splits the rows into independents and dependents'''
  #this is kind of crude, but it'll work for now
  rows = [row for row in table]
  #we use [1:-1] because I'm assuming 1 is the name of the row
  independents = []
  dependents = []
  for row in rows:
    new = []
    for item in row[1:-1]:
      if item:
        new.append(int(item))
      else:
        new.append(0)
    independents.append(new)
    dependents.append([int(row[-1])])
  return independents, dependents

def analyze(csv):
  table = Table(csv)
  mr = MultipleRegression(*split(table))
  pairs = [pair for pair in zip(table.fieldnames[1:-1], mr.coefficients)]
  pairs.sort(key=lambda x: -x[1])
  print
  for pair in pairs:
    print pair[0].strip(), pair[1][0]
  print len(pairs)

if __name__ == '__main__':
  if len(sys.argv) == 2:
    analyze(sys.argv[1])
