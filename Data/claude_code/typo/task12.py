from collections import deque

def bfs(graph, start):
    seen = {start}
    q = deque([start])
    result = []
    while q:
        curr = q.popleft()
        result.append(curr)
        for neighbor in graph[curr]:
            if neighbor not in seen:
                seen.add(neighbor)
                q.append(neighbor)
    return result
