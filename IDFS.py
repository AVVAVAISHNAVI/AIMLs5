def dfs_limited(graph, node, limit, visited):
    if limit < 0:
        return False
    print(node, end=" ")
    visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs_limited(graph, neighbor, limit - 1, visited):
                return True
    return False

def idfs(graph, start, depth):
    for limit in range(depth + 1):
        print(f"Depth {limit}: ", end="")
        if dfs_limited(graph, start, limit, set()):
            return
        print()

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
idfs(graph, 'A', 3)
