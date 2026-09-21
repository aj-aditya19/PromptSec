import heapq

def shortest_paths(network, starting_vertex):
	distances = {vertex: float('inf') for vertex in network}
	distances[starting_vertex] = 0
	pending = [(0, starting_vertex)]
	while pending:
		cost, vertex = heapq.heappop(pending)
		if cost != distances[vertex]:
			continue
		for neighbor, weight in network[vertex].items():
			candidate = cost + weight
			if candidate < distances.get(neighbor, float('inf')):
				distances[neighbor] = candidate
				heapq.heappush(pending, (candidate, neighbor))
	return distances
