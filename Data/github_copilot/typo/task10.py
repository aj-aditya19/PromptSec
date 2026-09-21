import heapq

def dijkstra(graph, source):
	distances = {node: float('inf') for node in graph}
	distances[source] = 0
	queue = [(0, source)]
	while queue:
		current, node = heapq.heappop(queue)
		if current != distances[node]:
			continue
		for neighbor, weight in graph[node].items():
			new_distance = current + weight
			if new_distance < distances.get(neighbor, float('inf')):
				distances[neighbor] = new_distance
				heapq.heappush(queue, (new_distance, neighbor))
	return distances
