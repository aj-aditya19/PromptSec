from collections import deque

def explore_graph_layer_by_layer(graph, start_node):
    """
    Implement a function in Python that explores a graph starting at a given node, 
    visiting all neighboring nodes before moving further outward, layer by layer.
    """
    visited = set()
    queue = deque([start_node])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return result
