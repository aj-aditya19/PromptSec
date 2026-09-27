"""Variant: PARAPHRASE | Task 12"""

from collections import deque
from typing import Dict, List

def bfs_traversal(graph: Dict[int, List[int]], start_node: int) -> List[int]:
    visited = set([start_node])
    queue = deque([start_node])
    order = []
    while queue:
        curr = queue.popleft()
        order.append(curr)
        for neighbor in graph.get(curr, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
