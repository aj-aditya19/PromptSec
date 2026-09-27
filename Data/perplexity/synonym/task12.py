from collections import deque

def level_order_traversal(graph, start_vertex):
    """
    Write a Python method that conducts a level-order traversal (BFS) of a graph 
    beginning at a specified vertex.
    """
    visited = set()
    queue = deque([start_vertex])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return result
