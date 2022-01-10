#topological sort of a graph is just a breadth first search
#might be worth learning to do this through DFS too
#need to push to github
#time = O(V+E)
#space = O(V+E)
from collections import deque

def solution(vertices, edges):
    
    sorted_order = []
    
    adjacency_list = {i:[] for i in range(vertices)}
    in_degree = {i:0 for i in range(vertices)}
    
    for i in range(len(edges)):
        adjacency_list[edges[i][0]].append(edges[i][1])
        in_degree[edges[i][1]] += 1
    
    sources = deque()
    
    for i in in_degree:
        if in_degree[i] == 0:
            sources.append(i)
            
    while sources:
        source = sources.popleft()
        children = adjacency_list[source]
        for i in children:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                sources.append(i)
        sorted_order.append(source)
    
    if len(sorted_order) != vertices:
        return []
    
    return(sorted_order)
    
print(solution(5, [[0, 1], [1,2], [2,3], [1,4]]))