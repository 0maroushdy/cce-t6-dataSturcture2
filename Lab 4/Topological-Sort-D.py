import sys
from heapq import heappush, heappop

def topological_sort():
    n, m = map(int, sys.stdin.readline().split())
    graph = {i: [] for i in range(n)}
    in_degree = [0] * n

    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        in_degree[v] += 1

    heap = []
    for u in range(n):
        if in_degree[u] == 0:
            heappush(heap, (-u, u))  # Max-heap using negative values

    result = []
    while heap:
        _, u = heappop(heap)
        result.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heappush(heap, (-v, v))

    if len(result) != n:
        print("The graph contains a cycle.")
    else:
        print(' '.join(map(str, result)))

topological_sort()