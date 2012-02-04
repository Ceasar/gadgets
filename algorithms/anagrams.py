from collections import defaultdict

PRIMES = {
    'a': 2,
    'b': 3,
    'c': 5,
    'd': 7,
    'e': 11,
    'f': 13,
    'g': 17,
    'h': 19,
    'i': 23,
    'j': 29,
    'k': 31,
    'l': 37,
    'm': 41,
    'n': 43,
    'o': 47,
    'p': 53,
    'q': 59,
    'r': 61,
    's': 67,
    't': 71,
    'u': 73,
    'v': 79,
    'w': 83,
    'x': 89,
    'y': 97,
    'z': 101
    }


def hash_func(word):
  product = 1
  for char in word:
    product *= PRIMES[char]
  return product


def anagrams(words):
  """
  Find all the anagrams in a list of words.

  >>> words = ['kinship', 'pinkish', 'boaster', 'boaters', 'borates']
  >>> anagrams(words)
  [['kinship', 'pinkish'], ['boaster', 'boaters', 'borates']]
  """
  anagrams = defaultdict(list)
  for word in words:
    anagrams[hash_func(word)].append(word)
  return anagrams.values()

if __name__ == "__main__":
  import doctest
  doctest.testmod()
