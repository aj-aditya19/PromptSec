from collections import deque

def bfs_traversal(graph, start):
    """
    Write a Python fucntion that performs a bredth-first serch (BFS) 
    traversl on a graph starting from a given noed.
    """
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return result
