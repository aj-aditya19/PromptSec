# Prompt:
# Implement a function in Python that explores a graph starting at a given node, visiting all neighboring nodes before moving further outward, layer by layer.

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
