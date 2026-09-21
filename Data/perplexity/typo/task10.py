# Prompt:
# Write a Python fucntion that implements Djikstra's algorithm to find the shrtest path from a source node to all othr nodes in a weighted graf.

# Python solution below

import heapq

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    heap = [(0, source)]
    while heap:
        distance, node = heapq.heappop(heap)
        if distance != distances[node]:
            continue
        for neighbor, weight in graph.get(node, []):
            candidate = distance + weight
            if candidate < distances.get(neighbor, float('inf')):
                distances[neighbor] = candidate
                heapq.heappush(heap, (candidate, neighbor))
    return distances
