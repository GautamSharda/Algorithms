import heapq
import math

def dijkstra(adj, start):
    
    #initialize bfs
    visited = set() 
    heap = [] #priority queue 
     #2d array to store shortest path weigh + optimal parent (which is initialized as non-existent]:
    res = [[math.inf, 0] for i in range(len(adj))]
    #start bfs from start node
    heapq.heappush(heap, (0, start))
    visited.add(start)
    res[start][0] = 0 #start to start has a path weight of 0
    
    #do a bfs
    #store (1. shortest weight from start to each node) and (2. optimal parent for each node) in res
    while heap:
        node = heapq.heappop(heap)[1]
        
        #best path weight so far
        weight = res[node][0]

        for edge in adj[node]:
            n, w = edge
            if n not in visited:
                heapq.heappush(heap, (w, n)) #push based on relative weight -- this is the key idea
                visited.add(n)
                #since this node has never been visited before, the current path is best so far
                res[n][0] = weight+w 
                res[n][1] = node
            #check if this path weight would be better, even if you've already visited this node
            if res[n][0] > weight+w:
                res[n][0] = weight+w
                res[n][1] = node
    
    #construct paths using optimal parent for each node (paths will be backwards, but that's ok)
    paths = []
    for i in range(1, 8):
        path = []
        next_ = i
        while next_ != 0:
            path.append(next_)
            next_ = res[next_][1]
        paths.append(path)
    return res, paths
    
    #conclusion:
    #res[index][0] contains weight of shortest path from start to node (index)
    #paths[index] contains ordered vertices forming shortest path from node (index) to start
    #time complexity of just finding the weights (traditional dijkstra): O(V + E*logV)
    #but actually constructing paths (variant) increases complexity to O(v^2) i think
    #couldn't find anything online to confirm that second time complexity
    
adj = [[], [(2, 2), (3, 1)], [(1, 2), (4, 11), (5, 3)], [(1, 1), (6, 15), (5, 1)], [(2, 11), (5, 2),
(7, 1)], [(2, 3), (3, 1), (4, 2), (6, 4), (7, 5)], [(3, 15), (5, 4), (7, 1)], [(5, 5), (4, 1), (6, 15)]]

print(dijkstra(adj, 7))
