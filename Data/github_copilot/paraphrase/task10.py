import heapq

def calculate_shortest_distances(graph, start):
	distances = {node: float('inf') for node in graph}
	distances[start] = 0
	queue = [(0, start)]
	while queue:
		distance, node = heapq.heappop(queue)
		if distance != distances[node]:
			continue
		for neighbor, weight in graph[node].items():
			candidate = distance + weight
			if candidate < distances.get(neighbor, float('inf')):
				distances[neighbor] = candidate
				heapq.heappush(queue, (candidate, neighbor))
	return distances
