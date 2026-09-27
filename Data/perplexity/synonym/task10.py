import heapq
from collections import defaultdict

def dijkstra_shortest_path(graph, start_vertex):
    """
    Write a Python method that applies Dijkstra's approach to determine the 
    minimum-cost route from a starting vertex to all other vertices in a weighted network.
    """
    distances = defaultdict(lambda: float('inf'))
    distances[start_vertex] = 0
    pq = [(0, start_vertex)]
    visited = set()

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dict(distances)
