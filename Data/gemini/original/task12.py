# Write a Python function that performs a breadth-first search (BFS) traversal on a graph starting from a given node.

from collections import deque

def bfs_traversal(graph: dict, start_node) -> list:
    visited = set([start_node])
    queue = deque([start_node])
    traversal_order = []

    while queue:
        node = queue.popleft()
        traversal_order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order
