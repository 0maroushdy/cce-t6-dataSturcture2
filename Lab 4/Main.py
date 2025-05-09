#!/usr/bin/env python3
"""
assignment4.py

This script implements two graph algorithms:
1. Topological Sort for Directed Acyclic Graphs (DAGs)
2. Minimum Spanning Tree (MST) using Prim's Algorithm on weighted undirected graphs

Usage:
  python assignment4.py topo < input.txt    # for topological sort
  python assignment4.py mst  < input.txt    # for MST via Prim's algorithm

Input Formats:
- Topological Sort:
   First line: n m   (number of vertices, number of edges)
   Next m lines: u v  (directed edge from u to v; 0-based vertices)

- MST (Prim):
   First line: n m   (number of vertices, number of edges)
   Next m lines: u v w  (edge between u and v with weight w; 0-based vertices)
   Next line: s     (starting vertex for Prim's algorithm)

Outputs:
- Topological Sort: prints vertices in one valid topological order or a cycle message.
- MST: prints MST edges and their weights, or a disconnected message.
"""
import sys
from collections import defaultdict, deque
import heapq

def topological_sort():
    data = sys.stdin.read().strip().split()
    if not data:
        print("No input provided for topological sort.")
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    graph = defaultdict(list)
    in_degree = [0] * n

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        graph[u].append(v)
        in_degree[v] += 1

    # Use deque for lexicographically smallest order
    queue = deque([u for u in range(n) if in_degree[u] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(topo_order) != n:
        print("The graph contains a cycle.")
    else:
        print(' '.join(map(str, topo_order)))


def prim_mst():
    data = sys.stdin.read().strip().split()
    if not data:
        print("No input provided for MST.")
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    graph = defaultdict(list)

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = float(next(it))
        graph[u].append((v, w))
        graph[v].append((u, w))

    s = int(next(it))

    # Prim's algorithm initialization
    in_mst = [False] * n
    keys = [float('inf')] * n
    parent = [-1] * n
    keys[s] = 0
    heap = [(0, s)]  # (key, vertex)
    mst_edges = []

    while heap:
        key_u, u = heapq.heappop(heap)
        if in_mst[u]:
            continue
        in_mst[u] = True
        if parent[u] != -1:
            mst_edges.append((parent[u], u, key_u))
        for v, weight in graph[u]:
            if not in_mst[v] and weight < keys[v]:
                keys[v] = weight
                parent[v] = u
                heapq.heappush(heap, (weight, v))

    # Check connectivity
    if len(mst_edges) != n - 1:
        print("No MST: Graph is disconnected.")
    else:
        # Sort edges for consistent output
        for u, v, w in sorted(mst_edges):
            print(f"{u} - {v} : {w}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python assignment4.py [topo|mst] < input.txt")
        sys.exit(1)
    mode = sys.argv[1].lower()
    if mode == 'topo':
        topological_sort()
    elif mode == 'mst':
        prim_mst()
    else:
        print(f"Unknown mode '{mode}'. Use 'topo' or 'mst'.")
        sys.exit(1)
