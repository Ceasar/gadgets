"""An algorithm for determining how many ways one can create an amount of
change given coins of different values."""

def change(amount, coins):
  '''Get the number of ways to get change for amount using coins.
  
  >>> coins = set([1, 5, 10])
  >>> change(10, coins)
  4
  >>> change(100, coins)
  121
  '''
  assert len(set(coins)) == len(coins), 'Coins must be unique'
  if 0 in coins:
  	return float('inf')
  #store the amount of ways we can generate x change, up to amount
  ways = [0] * amount 
  for coin in sorted(coins, reverse=True):
    increment = 1
    #iterate up to amount, jumping by the value of the coin
    for subamount in xrange(coin-1, amount, coin):
      ways[subamount] += increment
      increment = ways[subamount]
  return ways[-1]

if __name__ == "__main__":
	import doctest
	doctest.testmod()
