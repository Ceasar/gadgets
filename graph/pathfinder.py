from priority_dict import priority_dict

class UnreachableError(Exception):
    pass

def reconstruct_path(predecessor, goal, start=None):
    '''Reconstruct the path taken to a goal.

    >>> p = {'y': 'w', 'x': 'a', 'b': 'w', 'w': 'a'}
    >>> reconstruct_path(p, 'b')
    ['a', 'w', 'b']
    '''
    try:
        path = reconstruct_path(predecessor, predecessor[goal]) + [goal]
    except KeyError:
        path = [goal]
    if start is None or start in path:
        return path
    else:
        raise UnreachableError('%s is unreachable from %s' % (goal, start))


def bfs(graph, start, goal):
    '''Perform a breadth-first search to the goal.

    >>> graph = {'a': {'w': 14, 'x': 7, 'y': 9},
            'b': {'w': 9, 'z': 6},
            'w': {'a': 14, 'b': 9, 'y': 2},
            'x': {'a': 7, 'y': 10, 'z': 15},
            'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11},
            'z': {'b': 6, 'x': 15, 'y': 11}}
    >>> bfs(graph, 'a', 'b')
    ['a', 'w', 'b']
    '''
    predecessor = {}
    frontier = [start]
    explored = set()

    for node in iter(frontier):
        if node == goal: break
        for neighbor in graph[node]:
            if neighbor in explored: continue
            frontier.append(neighbor)
            predecessor[neighbor] = node
        explored.add(node)
    return reconstruct_path(predecessor, goal, start)


def dfs(graph, start, goal):
    '''Perform a depth-first search to the goal.

    >>> graph = {'a': {'w': 14, 'x': 7, 'y': 9},
            'b': {'w': 9, 'z': 6},
            'w': {'a': 14, 'b': 9, 'y': 2},
            'x': {'a': 7, 'y': 10, 'z': 15},
            'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11},
            'z': {'b': 6, 'x': 15, 'y': 11}}
    >>> dfs(graph, 'a', 'b')
    ['a', 'y', 'x', 'z', 'b']
    '''
    predecessor = {}  
    frontier = [start]
    explored = set()

    while frontier:
        node = frontier.pop()
        if node == goal: break
        for neighbor in graph[node]:
            if neighbor in frontier or neighbor in explored:
                continue
            frontier.append(neighbor)
            predecessor[neighbor] = node
        explored.add(node)
    return reconstruct_path(predecessor, goal, start)


def dijkstra(graph, start, goal, heuristic=lambda x, y: 0):
    '''
    Find the shortest path from start to goal.

    >>> graph = {'a': {'w': 14, 'x': 7, 'y': 9},
            'b': {'w': 9, 'z': 6},
            'w': {'a': 14, 'b': 9, 'y': 2},
            'x': {'a': 7, 'y': 10, 'z': 15},
            'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11},
            'z': {'b': 6, 'x': 15, 'y': 11}}
    >>> dijkstra(graph,'a','b')
    ['a', 'y', 'w', 'b']

    By supplying a heuristic, you can transform the algorithm into the
    a* search algorithm.
    '''
    predecessor = {}
    frontier = priority_dict({start: 0})
    explored = set()
    
    traveled = {start: 0}
    remaining = {start: heuristic(start, goal)} #cached for speed

    for nearest in frontier.sorted_iter():
        if nearest == goal: break
        explored.add(nearest)
        for neighbor in graph[nearest]:
            if neighbor in explored: continue
            displacement = traveled[nearest] + graph[nearest][neighbor]
            if neighbor in frontier and displacement > traveled[neighbor]:
                continue
            traveled[neighbor] = displacement
            if not neighbor in remaining:
                remaining[neighbor] = heuristic(neighbor, goal)
            frontier[neighbor] = displacement + remaining[neighbor]
            predecessor[neighbor] = nearest
        del traveled[nearest]
    return reconstruct_path(predecessor, goal, start)

