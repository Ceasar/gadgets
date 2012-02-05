from collections import defaultdict, Counter


def anagrams(words):
  """
  Find all the anagrams in a list of words.

  >>> words = ['kinship', 'pinkish', 'boaster', 'boaters', 'borates']
  >>> anagrams(words)
  [['kinship', 'pinkish'], ['boaster', 'boaters', 'borates']]
  """
  anagrams = defaultdict(list)
  for word in words:
    anagrams[tuple(Counter(word).items())].append(word)
  return anagrams.values()

if __name__ == "__main__":
  import doctest
  doctest.testmod()
