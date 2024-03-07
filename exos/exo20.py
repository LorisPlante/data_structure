#  Implémentez le parcours en profondeur (DFS) sur un graphe représenté par un dictionnaire.

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited