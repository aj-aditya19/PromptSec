import heapq

def dijkstra(graph, source):
	distances = {node: float('inf') for node in graph}
	distances[source] = 0
	pending = [(0, source)]
	while pending:
		distance, node = heapq.heappop(pending)
		if distance != distances[node]:
			continue
		for neighbor, weight in graph[node].items():
			candidate = distance + weight
			if candidate < distances.get(neighbor, float('inf')):
				distances[neighbor] = candidate
				heapq.heappush(pending, (candidate, neighbor))
	return distances
