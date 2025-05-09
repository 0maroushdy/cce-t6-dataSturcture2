import heapq
from collections import defaultdict

def prim_mst(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start, None)]  # (weight, current_vertex, parent)

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        if parent is not None:
            mst.append((parent, u, weight))
        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (w, v, u))
    
    return mst

# Example usage:
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)],
}

mst_edges = prim_mst(graph, 'A')
print("MST edges:", mst_edges)
