from collections import defaultdict

from pathfinder import bfs
from priority_dict import priority_dict


class NotConnectedError(Exception):
    pass

def connected(graph):
    '''Check if the graph is connected.'''
    frontier = [iter(graph).next()]
    explored = set()

    for node in iter(frontier):
        for neighbor in graph[node]:
            if neighbor in explored: continue
            frontier.append(neighbor)
        explored.add(node)
    return explored == set(graph)


def reconstruct_tree(graph, predecessor):
    '''Build a tree from a list of predecessors.'''
    tree = defaultdict(dict)
    for node in predecessor:
        source = predecessor[node]
        tree[node][source] = tree[source][node] = graph[node][source]
    return dict(tree)

def prim(graph):
    '''
    >>> graph = {'a': {'b': 7, 'd': 5},
            'b': {'a': 7, 'c': 8, 'd': 9, 'e': 7},
            'c': {'b': 8, 'e': 5},
            'd': {'a': 5, 'e': 15, 'f': 6},
            'e': {'b': 7, 'c': 5, 'd': 15, 'f': 8, 'g': 9},
            'f': {'d': 6, 'e': 8, 'g': 11},
            'g': {'e': 9, 'f': 11}}
    >>> prim(graph)
    {'d': {'a': 5, 'f': 6},
    'a': {'b': 7},
    'b': {'e': 7},
    'e': {'c': 5, 'g': 9}}
    '''
    if not connected(graph): raise NotConnectedError('graph is not connected')

    predecessor = {}
    frontier = priority_dict({iter(graph).next(): 0})
    explored = set()

    for nearest in frontier.sorted_iter():
        for neighbor in graph[nearest]:
            if neighbor in explored: continue
            displacement = graph[nearest][neighbor]
            if neighbor in frontier and displacement > frontier[neighbor]:
                continue
            else:
                frontier[neighbor] = displacement
                predecessor[neighbor] = nearest
        explored.add(nearest)
    return reconstruct_tree(graph, predecessor)


def edges(graph):
    '''Get all of the edges in a graph.'''
    edges = {}
    for node in graph:
        for neighbor in graph[node]:
            edges[frozenset([node, neighbor])] = graph[node][neighbor]
    return edges
    
def krusgal(graph):
    '''
    >>> graph = {'a': {'b': 7, 'd': 5},
            'b': {'a': 7, 'c': 8, 'd': 9, 'e': 7},
            'c': {'b': 8, 'e': 5},
            'd': {'a': 5, 'e': 15, 'f': 6},
            'e': {'b': 7, 'c': 5, 'd': 15, 'f': 8, 'g': 9},
            'f': {'d': 6, 'e': 8, 'g': 11},
            'g': {'e': 9, 'f': 11}}
    >>> krusgal(graph)
    {'a': {'b': 7, 'd': 5},
    'c': {'e': 5},
    'b': {'a': 7, 'e': 7},
    'e': {'c': 5, 'b': 7, 'g': 9},
    'd': {'a': 5, 'f': 6}, 'g': {'e': 9},
    'f': {'d': 6}}
    '''
    if not connected(graph): raise NotConnectedError('graph is not connected')

    tree = defaultdict(dict)
    edge_length = edges(graph)

    edge_count = 0
    while edge_count < len(graph) - 1:
        a, b = min(edge_length, key=lambda edge: edge_length[edge])
        #Check for a cycle
        try:
            path = bfs(tree, a, b)
        except:
            tree[a][b] = tree[b][a] = graph[a][b]
            edge_count += 1
        finally:
            edge_length.pop(frozenset([a, b]))
    return dict(tree)
