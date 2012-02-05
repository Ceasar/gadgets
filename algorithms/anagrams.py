from collections import defaultdict, Counter


def anagrams(words):
  """
  Find all the anagrams in a list of words.

  >>> words = ['bon', 'boon', 'bono', 'nob']
  >>> anagrams(words)
  [['boon', 'bono'], ['bon', 'nob']]
  """
  anagrams = defaultdict(list)
  for word in words:
    anagrams[tuple(Counter(word).iteritems())].append(word)
  return anagrams.values()

if __name__ == "__main__":
  import doctest
  doctest.testmod()
