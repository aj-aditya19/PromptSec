from collections import deque

def traverse_by_levels(graph, start_node):
	visited = {start_node}
	pending = deque([start_node])
	traversal = []
	while pending:
		node = pending.popleft()
		traversal.append(node)
		for neighbor in graph.get(node, []):
			if neighbor not in visited:
				visited.add(neighbor)
				pending.append(neighbor)
	return traversal
