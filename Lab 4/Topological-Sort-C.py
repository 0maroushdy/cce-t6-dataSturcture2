from collections import defaultdict, deque

def topological_sort(vertices, edges):
    graph = defaultdict(list)
    in_degree = {v: 0 for v in vertices}
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([v for v in vertices if in_degree[v] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) != len(vertices):
        raise ValueError("Graph is not a DAG")
    
    return topo_order

# Example usage:
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [('A', 'C'), ('B', 'C'), ('C', 'D'), ('D', 'E')]
print(topological_sort(vertices, edges))
