# Prompt:
# Write a Python function that implements Dijkstra's algorithm to find the shortest path from a source node to all other nodes in a weighted graph.

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
