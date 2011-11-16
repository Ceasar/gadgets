"""An algorithm for determining how many ways one can create an amount of
change given coins of different values."""

def change(amount, coins):
  '''Get the number of ways to get change for amount using coins.
  
  >>> coins = set([1, 2, 5, 10, 20, 50, 100, 200])
  >>> change(200, coins)
  73682
  '''
  assert len(set(coins)) == len(coins), 'Coins must be unique'
  if 0 in coins:
    return float('inf')
  ways = [1] + [0] * amount
  for coin in sorted(coins, reverse=True):
    for subamount in xrange(coin, amount+1):
      ways[subamount] += ways[subamount-coin]
  return ways[-1]

if __name__ == "__main__":
  import doctest
  doctest.testmod()
