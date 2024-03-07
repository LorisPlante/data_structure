from exos.exo20 import dfs
def test_dfs():
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }
    assert dfs(graph, 'A') == {'A', 'B', 'D', 'E', 'C', 'F'}
    assert dfs(graph, 'C') == {'C', 'A', 'B', 'D', 'E', 'F'}
    assert dfs(graph, 'E') == {'E', 'B', 'A', 'C', 'F', 'D'}
    assert dfs(graph, 'F') == {'F', 'C', 'A', 'B', 'D', 'E'}
    assert dfs(graph, 'B') == {'B', 'A', 'C', 'F', 'E', 'D'}
    assert dfs(graph, 'D') == {'D', 'B', 'A', 'C', 'F', 'E'}