graph={
    "5" : ["3", "7"],
    "3" : ["2", "4"],
    "7" : ["8"],
    "2" : [],
    "4" : ["8"],
    "8" : []
}

visited=[]
queue=[]

def BFS(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
     m=queue.pop()
     print(m,end =" ")

    for neighbour in graph[m]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)


print("following is the breadth first search")
BFS(visited,graph,'5')


# graph={
#     "5" : ["3", "7"],
#     "3" : ["2", "4"],
#     "7" : ["8"],
#     "2" : [],
#     "4" : ["8"],
#     "8" : []
# }

# visited=[]
# queue=[]

# def bfs(visited,graph,node):
#   visited.append(node)
#   queue.append(node)

#   while queue:
#     m=queue.pop(0)
#     print(m,end ="")

#     for neighbour in graph[m]:
#         if neighbour not in visited:
#            visited.append(neighbour)
#            queue.append(neighbour)

# print("The following is the breadth first search") 
# bfs(visited, graph, '5')