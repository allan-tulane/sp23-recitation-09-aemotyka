from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    def path_helper(visited, frontier, graph):
      if len(frontier) == 0:
        return visited
      else:
        distance, node, edges = heappop(frontier)
        if node in visited:
          return path_helper(visited, frontier)
        else:
          visited[node] = (distance, edges)
          for neighbor_node, node_weight in graph[node]:
            heappush(frontier, (distance + node_weight, neighbor_node, edges + 1))
          return path_helper(visited, frontier, graph)

    frontier = []
    visited = {}
    heappush(frontier, (0, source, 0))
    return path_helper(visited, frontier, graph)
    
def test_shortest_shortest_path():

    graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
    result = shortest_shortest_path(graph, 's')
    # result has both the weight and number of edges in the shortest shortest path
    assert result['s'] == (0,0)
    assert result['a'] == (1,1)
    assert result['b'] == (3,2)
    assert result['c'] == (4,1)
    assert result['d'] == (7,2)
    
    
def bfs_path(graph, source):
  parent = {}
  for i in graph:
    parent[i] = None
  parent[source] = source
  visited = set([source])
  frontier = [source]

  while len(frontier) > 0:
    node = frontier.pop(0)
    for j in graph[node]:
      if j not in visited:
        parent[j] = node
        visited.add(j)
        frontier.append(j)

  return parent
      

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert parents['a'] == 's'
    assert parents['b'] == 's'    
    assert parents['c'] == 'b'
    assert parents['d'] == 'c'

def get_path(parents, destination):
  path = []
  node = destination

  while node != parents[node]:
    node = parents[node]
    path.append(node)

  path.reverse()
  ret = ""
  
  for i in path: ret+=i
    
  return ret
  
def test_nodepath():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert get_path(parents, 'd') == 'sbc'
