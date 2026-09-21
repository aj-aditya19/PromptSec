import heapq

def shortest_paths(network, start_vertex):
    min_cost = {vertex: float('inf') for vertex in network}
    min_cost[start_vertex] = 0
    frontier = [(0, start_vertex)]
    while frontier:
        cost, vertex = heapq.heappop(frontier)
        if cost > min_cost[vertex]:
            continue
        for neighbor, edge_weight in network[vertex].items():
            new_cost = cost + edge_weight
            if new_cost < min_cost[neighbor]:
                min_cost[neighbor] = new_cost
                heapq.heappush(frontier, (new_cost, neighbor))
    return min_cost
