import sys
import heapq

def prim_mst():
    n, m = map(int, sys.stdin.readline().split())
    graph = {i: [] for i in range(n)}

    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))  # Undirected graph

    s = int(sys.stdin.readline())

    keys = [float('inf')] * n
    parents = [-1] * n
    keys[s] = 0
    heap = []
    heapq.heappush(heap, (0, s))
    in_mst = [False] * n
    mst_edges = []

    while heap:
        current_key, u = heapq.heappop(heap)
        if in_mst[u]:
            continue
        in_mst[u] = True
        if parents[u] != -1:
            mst_edges.append((parents[u], u, current_key))

        for v, weight in graph[u]:
            if not in_mst[v] and weight < keys[v]:
                keys[v] = weight
                parents[v] = u
                heapq.heappush(heap, (weight, v))

    if len(mst_edges) != n - 1:
        print("No MST: Graph is disconnected.")
    else:
        for u, v, w in mst_edges:
            print(f"{u} - {v} : {w}")

prim_mst()