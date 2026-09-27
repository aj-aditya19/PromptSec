import heapq
from collections import defaultdict

def dijkstra(graph, start):
    """
    Write a Python fucntion that implements Djikstra's algorithm to find the 
    shrtest path from a source node to all othr nodes in a weighted graf.
    """
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    pq = [(0, start)]
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
