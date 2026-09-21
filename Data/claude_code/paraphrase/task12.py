from collections import deque

def explore_graph_by_layer(graph, start_node):
    visited_nodes = set()
    visited_nodes.add(start_node)
    to_visit = deque([start_node])
    traversal = []
    while to_visit:
        current = to_visit.popleft()
        traversal.append(current)
        for neighbor in graph.get(current, []):
            if neighbor not in visited_nodes:
                visited_nodes.add(neighbor)
                to_visit.append(neighbor)
    return traversal
