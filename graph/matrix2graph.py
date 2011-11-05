from collections import defaultdict
from itertools import product

from pathfinder import bfs, dfs, dijkstra


#These should be changed depending on what kind of movement is permitted
DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0))

def matrix2graph(matrix):
  graph = defaultdict(dict)
  for x, y, in matrix:
    if matrix[y][x] != 1:
      print matrix[y][x]
      for direction in DIRS:
        dx, dy = direction
        neighbor = ((x + dx) % len(matrix[0]), (y + dy) % len(matrix))
        graph[neighbor][x, y] = 1
  return dict(graph)

if __name__ == '__main__':
  a = [[0, 1], [0, 0]]
  b = matrix2graph(a)
  for c in a:
    print c
  for c in b:
    print c, b[c]
