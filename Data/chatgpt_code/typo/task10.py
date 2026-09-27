import heapq

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    heap = [(0, source)]

    while heap:
        distance, node = heapq.heappop(heap)
        if distance != distances[node]:
            continue
        for neighbor, weight in graph[node]:
            new_distance = distance + weight
            if new_distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))
    return distances
