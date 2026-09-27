import heapq
from collections import defaultdict

def calculate_minimum_distances(weighted_graph, starting_point):
    """
    Implement a function in Python that, given a weighted graph and a starting point, 
    calculates the cheapest possible distance to reach every other point in the graph.
    """
    distances = defaultdict(lambda: float('inf'))
    distances[starting_point] = 0
    pq = [(0, starting_point)]
    visited = set()

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in weighted_graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dict(distances)
