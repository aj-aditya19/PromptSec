# Prompt:
# Write a Python function that performs a breadth-first search (BFS) traversal on a graph starting from a given node.

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
