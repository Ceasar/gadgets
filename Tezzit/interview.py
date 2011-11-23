#!/usr/bin/env python

import random # for seed, random
import sys    # for stdout

GAP_COST = -2
MATCH_SCORE = 1
MISMATCH_SCORE = -1

def score(top, bot):
  '''Score two elements.'''
  if top == bot:
      return MATCH_SCORE
  elif top == " " or bot == " ":
    return GAP_COST
  else: #top != bot
    return MISMATCH_SCORE


def init_graph(m, n):
  '''Initialize a m by n graph. Returns start and end.'''
  graph = {}
  for i in range(m + 1):
    graph[i] = {}
  graph[0][0] = Node(0, 0)
  for i in range(1, m + 1):
    graph[i][0] = Node(i, 0)
    graph[i-1][0].distanceto[graph[i][0]] = GAP_COST
  for j in range(1, n + 1):
    graph[0][j] = Node(0, j)
    graph[0][j-1].distanceto[graph[0][j]] = GAP_COST
  return graph


##def init_matrix_copy(m, n):
##  matrix = {}
##  for i in range(m + 1):
##    matrix[i] = {}
##  matrix[0][0] = 0
##  for i in range(1, m + 1):
##    matrix[i][0] = matrix[i-1][0] + GAP_COST
##  for j in range(1, n + 1):
##    matrix[0][j] = matrix[0][j-1]  + GAP_COST
##  return matrix


def build_graph(strand1, strand2):
  '''Build a graph.'''
  m = len(strand1)
  n = len(strand2)
  graph = init_graph(m, n)

  for i in range(1, m + 1):
    for j in range(1, n + 1):
      graph[i][j] = Node(i, j)
                             
      #Update North
      graph[i-1][j].distanceto[graph[i][j]] = GAP_COST
                             
      #Update West
      graph[i][j-1].distanceto[graph[i][j]] = GAP_COST

      #Update NorthWest
      top = strand1[i-1]
      bot = strand2[j-1]
      graph[i-1][j-1].distanceto[graph[i][j]] = score(top, bot)

  start = graph[0][0]
  end = graph[m][n]
  return (start, end)


##def build_graph_copy(strand1, strand2):
##  m = len(strand1)
##  n = len(strand2)
##  graph = init_matrix(m, n)
##
##  for i in range(1, m + 1):
##    for j in range(1, n + 1):
##      #First assume North
##      north = graph[i-1][j] + GAP_COST
##      best = north
##
##      #Try West
##      west = graph[i][j-1] + GAP_COST
##      if best < west:
##        best = west
##
##      #Try NorthWest
##      top = strand1[i-1]
##      bot = strand2[j-1]
##      northwest = graph[i-1][j-1] + score(top, bot)
##      if best < northwest:
##        best = northwest
##
##      graph[i][j] = best
##
##  return graph


def estimate(node, goal):
  '''Estimate the cost of traveling from the node to the goal.'''
  dy = goal.loc[0] - node.loc[0]
  dx = goal.loc[1] - node.loc[1]
  return min(dx, dy) * -0.5 + (max(dx, dy) - min(dx, dy)) * -2


def closest(openset, etotal):
  '''Get the node closest to the goal.'''
  best = float('-inf')
  best_node = None
  for node in openset:
    if etotal[node] > best:
      best = etotal[node]
      best_node = node
  return best_node


def path(came_from, current_node):
  '''Reconstruct the path taken.'''
  try:
    p = path(came_from, came_from[current_node])
    p.append(current_node)
    return p
  except:
    return [current_node]


def a_star(start, goal):
  '''Quickly find the quickest path from start to goal.'''
  closedset = set()
  openset = set([start])
  came_from = {}

  dfs = {} #distance from start
  dfg = {} #distance from goal
  etotal = {} #estimated total distance

  dfs[start] = 0
  dfg[start] = estimate(start, goal)
  etotal[start] = dfg[start]

  while len(openset) > 0:
    lead = closest(openset, etotal)
    if lead == goal:
      return path(came_from, came_from[goal])

    openset.remove(lead)
    closedset.add(lead)
    for neighbor in lead.distanceto:
      if neighbor in closedset:
        continue
      tenative_dist = dfs[lead] + lead.distanceto[neighbor]
    
      if neighbor not in openset:
        openset.add(neighbor)
        tenative_is_better = True
      elif tenative_dist > dfs[neighbor]:
        tenative_is_better = True
      else:
        tenative_is_better = False

      if tenative_is_better:
        came_from[neighbor] = lead
        dfs[neighbor] = tenative_dist
        dfg[neighbor] = estimate(neighbor, goal)
        etotal[neighbor] = dfs[neighbor] + dfg[neighbor]

class Node(object):
  '''A node object.'''
  def __init__(self, i, j):
    self.loc = (i, j)
    self.distanceto = {}

  def __str__(self):
    return str(self.loc)


def get_diff(node1, node2):
  '''Get the differnce.'''
  dy = node2.loc[0] - node1.loc[0]
  dx = node2.loc[1] - node1.loc[1]
  return (dy, dx)


def score_strands(strand1, strand2):
  '''Score two strands.'''
  minlen = min(len(strand1), len(strand2)) #Should be equal
  total = 0
  for pos in range(minlen):
    top = strand1[pos]
    bot = strand2[pos]
    total += score(top, bot)
  return total

def build_strands(instructions, strand1, strand2):
  '''Build the two strands using a set of instructions.'''
  best_strand1 = ""
  best_strand2 = ""
  s1pos = 0
  s2pos = 0
  current = instructions.pop(0)
  while len(instructions) > 0:
    nextnode = instructions.pop(0)
    diff = get_diff(current, nextnode)
    #print current, diff, s1pos, s2pos
    if diff == (1, 1):
      best_strand1 += strand1[s1pos]
      s1pos += 1
      best_strand2 += strand2[s2pos]
      s2pos += 1
    elif diff == (0, 1):
      best_strand1 += " "
      best_strand2 += strand2[s2pos]
      s2pos += 1
    elif diff == (1, 0):
      best_strand2 += " "
      best_strand1 += strand1[s1pos]
      s1pos += 1
    current = nextnode
  return (best_strand1, best_strand2)
  

def findOptimalAlignment(strand1, strand2, cache):
  '''Compute the score of the optimal alignment of two DNA strands returns a list that includes the optimum elements.'''
  start, goal = build_graph(strand1, strand2)
  path = a_star(start, goal)
  strands = build_strands(path, strand1, strand2)
  score = score_strands(strands[0], strands[1])
  
  return strands + (score,)


def generateRandomDNAStrand(minlength, maxlength):
  '''Utility function that generates a random DNA string of a random length drawn from the range [minlength, maxlength]'''
  assert minlength > 0, \
       "Minimum length passed to generateRandomDNAStrand" \
       "must be a positive number" # these \'s allow mult-line statements
  assert maxlength >= minlength, \
       "Maximum length passed to generateRandomDNAStrand must be at " \
       "as large as the specified minimum length"
  strand = ""
  length = random.choice(xrange(minlength, maxlength + 1))
  bases = ['A', 'T', 'G', 'C']
  for i in xrange(0, length):
    strand += random.choice(bases)
  return strand


def printAlignment(best, out=sys.stdout):
  '''Takes a tuple best which contains strand1, strand2, alignmentscore and prints them.'''
  print best
  plus = "+ "
  minus = "- "
  minlen = min(len(best[0]), len(best[1]))
  maxlen = max(len(best[0]), len(best[1]))
  score = 0

  for i in range(0, minlen):
    top = best[0][i]
    bot = best[1][i]
    if top == bot:
      plus += "1"
      minus += " "
      score += 1
    elif top == " " or bot == " ":
      plus += " "
      minus += "2"
      score -= 2
    else:
      plus += " "
      minus += "1"
      score -= 1
      
  for j in range(minlen, maxlen):
    plus += " "
    minus += "2"
    score -= 2
  
  out.write("\nOptimal alignment score is " + str(score)+ "\n\n")
  out.write(plus+ "\n")
  out.write("  " + best[0] + "\n" + "  "+ best[1] + "\n") 
  out.write(minus + "\n\n")


# Unit test main in place to do little more than
# exercise the above algorithm.  As written, it
# generates two fairly short DNA strands and
# determines the optimal alignment score.
#
# As you change the implementation of findOptimalAlignment
# to use memoization, you should change the 8s to 40s and
# the 10s to 60s and still see everything execute very
# quickly.
def main():
  while (True):
    sys.stdout.write("Generate random DNA strands? ")
    answer = sys.stdin.readline()
    if answer == "no\n": break
    low = 300
    high = 500
    strand1 = generateRandomDNAStrand(low, high)
    strand2 = generateRandomDNAStrand(low, high)
    sys.stdout.write("Aligning these two strands: " + strand1 + "\n")
    sys.stdout.write("                            " + strand2 + "\n")
    cache = {}
    alignment = findOptimalAlignment(strand1, strand2, cache)
    printAlignment(alignment)
    
if __name__ == "__main__":
  main()
