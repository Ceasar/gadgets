from event import Probability, Event
from counting import Multiset

class Coin(Probability):
  def __init__(self, p=0.5):
    heads, tails = Event(['H']), Event(['T'])
    super(Coin, self).__init__({heads: p, tails: 1.0 - p})

class Die(Probability):
  def __init__(self, sides=6):
    p = {}
    for x in range(1, sides + 1):
      p[Event([x])] = 1.0 / sides
    super(Die, self).__init__(p)

class NumberedDeck(Multiset):
  '''A multiset of numbered cards from Ace to 2.'''

  cards = '234567890JQKA'

  def __init__(self):
    super(NumberedDeck, self).__init__()
    for card in self.cards:
      self[card] = 4

class SuitedDeck(Multiset):
  '''A multiset of suited cards.'''

  suits = ('spades', 'clubs', 'hearts', 'diamonds')

  def __init__(self):
    super(SuitedDeck, self).__init__()
    for suit in self.suits:
      self[suit] = 13
