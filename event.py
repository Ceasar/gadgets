from itertools import *

Event = frozenset #renaming this here for convenience

class Probability(dict):
  '''A space of states and their respective probabilities.'''

  #Axiom 1: 0 <= P(E) <= 1
  #Axiom 2: P(S) = 1
  #Axiom 3: If A and B are mutually exclusive, then
  # P(A, B) = P(A) + P(B)

  @property
  def sample_space(self):
    return self.keys()

  def __missing__(self, k):
    return 0.0

  #Proposition 4.1
  def complement(self, event):
    return 1.0 - self[event]

  #Proposition 4.3
  #none of
  def neither(self, *events):
    return 1.0 - self.union(*events)

  #Proposition 4.4 - Inclusion-Exclusion Identitiy
  #at least one of
  def union(self, *events):
    p = 0.0
    i = 1
    sign = 1
    while i <= len(events):
      for combination in combinations(events, i):
        p += sign * self[frozenset.union(*combination)]
      sign *= -1
      i += 1
    return p

  def disjoint(self, a, b):
    return self.probability(a & b) == 0
