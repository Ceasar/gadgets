from __future__ import division

from math import factorial
from itertools import *

from probability.counting import *
from probability.event import *
from probability.objects import *

def ex4a():
  A = Event(['A'])
  B = Event(['B'])
  P = Probability()
  P[A] = 0.5
  P[B] = 0.4
  P[A|B] = 0.3
  return P.neither(A, B)
print "ex4a", ex4a()

def ex5a():
  a = Die()
  #don't really like this code, but whatever...
  outcomes = set()
  sevens = set()
  for roll in product(a.sample_space, a.sample_space):
    outcomes.add(roll)
    total = 0
    for die in roll:
      total += sum(die)
    if total == 7:
      sevens.add(roll)
  return len(sevens) / len(outcomes)
print "ex5a", ex5a()

def ex5b():
  '''Given 6 white balls and 5 black balls, white is the probability that we have 1 white ball and 2 black balls after 3 draws?'''
  bag = Multiset({'white': 6, 'black': 5})
  return bag.draw({'white': 1, 'black': 2}, replacement=False)
print "ex5b", ex5b()

def ex5c():
  '''Given 6 men and 9 women, what is the probability that we have 3 men and two women after choosing 5?'''
  people = Multiset({'men': 6, 'women': 9})
  return people.draw({'men': 3, 'women': 2}, replacement=False)
print "ex5c", ex5c()

def ex5d(n, k):
  '''What is the probabilty of draw a special ball given k draws and n balls.'''
  balls = Multiset({'special': 1, 'others': n - 1})
  #comes out to k / n
  return balls.draw({'special': 1, 'others': k - 1})

def ex5f():
  '''What is the probability one is dealt a straight?'''
  deck = NumberedDeck()
  #this can be any straight- we just need to know the generic
  #probability for this to work
  straight = {'A': 1, '2': 1, '3': 1, '4': 1, '5': 1}
  return 10 * deck.draw(straight, replacement=False)
print "ex5f", ex5f()

def ex5g():
  '''What is the probability one is deal a full-house?

  A full house conists of one pair and a a three-of-a-kind.'''
  deck = NumberedDeck()
  #this can be any full-house- we just need to know the generic
  #probability
  full_house = {'A': 2, '2': 3}
  #13 ways to draw pair, leaves 12 ways to draw the 3-of-a-kind
  #(or vice-versa)
  return 13 * 12 * deck.draw(full_house, replacement=False)
print "ex5g", ex5g()

def ex5ha():
  '''What is the probability one player recieves all 13 spades given the deck is dealt out evenly among 4 players?'''
  deck = SuitedDeck()
  return 4 * deck.draw({'spades': 13}, replacement=False)
print "ex5ha", ex5ha()

def ex5hb():
  return factorial(4) * arrange(48, False, 12, 12, 12, 12)
print "ex5hb", ex5hb()
