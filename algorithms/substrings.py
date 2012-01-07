

def substrings(word):
  for i in xrange(len(word) + 1):
    for j in xrange(i+1, len(word) + 1):
      yield word[i:j]

