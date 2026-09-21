from collections import deque

def level_order_traversal(graph, start_vertex):
	visited = {start_vertex}
	pending = deque([start_vertex])
	order = []
	while pending:
		vertex = pending.popleft()
		order.append(vertex)
		for adjacent in graph.get(vertex, []):
			if adjacent not in visited:
				visited.add(adjacent)
				pending.append(adjacent)
	return order
