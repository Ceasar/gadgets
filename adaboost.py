from __future__ import division
from math import exp, log


data = [
    ((0.5, 3.5), 1),
    ((1.5, 2.5), 1),
    ((5.5, 5.5), 1),
    ((7.5, 7.5), 1),
    ((9.5, 6.5), 1),
    ((2.5, 1.5), -1),
    ((4.5, 4.5), -1),
    ((7.5, 3.5), -1),
    ((11.5, 1.5), -1),
    ((11.5, 6.5), -1)
    ]

hs = [
    lambda x1, x2: 1 if x1 >= 2 else -1,
    lambda x1, x2: 1 if x1 >= 5 else -1,
    lambda x1, x2: 1 if x1 >= 10 else -1,
    lambda x1, x2: 1 if x2 <= 2 else -1,
    lambda x1, x2: 1 if x2 <= 5 else -1,
    lambda x1, x2: 1 if x2 <= 10 else -1
    ]


def adaboost(data, classifiers, rounds):
  n = len(data)
  a = [0] * n
  h = [None] * n
  D = [[] for _ in data]
  D[0] = [1 / n for _ in data]
  x, y = zip(*data)
  for t in range(rounds):
    def error(h):
      '''Calculate the weighted percent of misclassified data.
      A higher score indicates a higher rate of misclassification.'''
      return sum(D[t][i] * int(y[i] != h(*x[i])) for i in range(n))
    e, h = min((error(h), h) for h in classifiers)
    h[t] = h
    a[t] = log((1 - e) / e) / 2
    z = sum(D[t][i] * exp(-a * y[i] * h(*x[i])) for i in range(n))
    D[t+1] = [D[t][i] * exp(-a * y[i] * h(*x[i])) / z for i in range(n)]
  return lambda x: 1 if sum(a[t] * h[t](x) for t in range(rounds)) > 0 else -1

