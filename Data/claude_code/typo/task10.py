import heapq

def dijkstra(graph, source):
    dist = {}
    for node in graph:
        dist[node] = float('inf')
    dist[source] = 0
    queue = [(0, source)]
    while queue:
        d, node = heapq.heappop(queue)
        if d > dist[node]:
            continue
        for neighbor in graph[node]:
            weight = graph[node][neighbor]
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor))
    return dist
