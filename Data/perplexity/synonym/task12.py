# Prompt:
# Write a Python method that conducts a level-order traversal (BFS) of a graph beginning at a specified vertex.

# Python solution below

from collections import deque

def bfs_traversal(graph, start):
    visited, order = {start}, []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
