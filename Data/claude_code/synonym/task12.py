from collections import deque

def level_order_traversal(network, start_vertex):
    explored = {start_vertex}
    pending = deque([start_vertex])
    visit_order = []
    while pending:
        vertex = pending.popleft()
        visit_order.append(vertex)
        for adjacent in network[vertex]:
            if adjacent not in explored:
                explored.add(adjacent)
                pending.append(adjacent)
    return visit_order
