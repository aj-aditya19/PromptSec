import heapq

def compute_shortest_distances(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    heap = [(0, start)]
    visited = set()
    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        for v, w in graph[u].items():
            if d + w < distance[v]:
                distance[v] = d + w
                heapq.heappush(heap, (distance[v], v))
    return distance
