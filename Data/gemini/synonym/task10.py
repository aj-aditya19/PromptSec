"""Variant: SYNONYM | Task 10"""

import heapq
from typing import Dict, List, Tuple

def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, float]:
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist > distances[curr_node]:
            continue
        for neighbor, weight in graph.get(curr_node, []):
            distance = curr_dist + weight
            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances
