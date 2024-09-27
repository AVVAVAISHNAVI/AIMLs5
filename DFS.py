graph={
    "5" : ["3", "7"],
    "3" : ["2", "4"],
    "7" : ["8"],
    "2" : [],
    "4" : ["8"],
    "8" : []
}

visited = set()

def DFS(visited,graph,node):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            DFS(visited,graph,neighbour)

print("depth first search")
DFS(visited,graph,'5')