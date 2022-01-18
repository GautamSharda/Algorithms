#max heap problem
#naive solution would be to find distances, then sort, which is N*log(n) time, O(n) space
#for max heap solution: 
#time = O(N*log(k)) -- because you push/pop N times and each takes log(K) time -- btw heapify is O(n), obviously n + n*logk = O(n*logk) still
#space = O(k) for heap and res -- k + k = 2k = O(k) 
import heapq

def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    
    #create max_heap with k elements "sorted" by distance
    max_heap = []
    for index in range(k):
        
        x, y = points[index]
        
        distance = x**2 + y**2
        
        max_heap.append([-distance, x, y])
        
    heapq.heapify(max_heap)
    
    #go through the rest of the elements adding one to the heap and popping the biggest with each iteration to be left with k smallest in the end -- could be combined with step above, but this is cleaner imo
    for index in range(k, len(points)):
        
        x, y = points[index]
        
        distance = x**2 + y**2
        
        heapq.heappush(max_heap, [-distance, x, y])
        heapq.heappop(max_heap)
    
    #cannot just return the heap because you need to extract the x,y since heap has distance, x, y -- but creating new list doesn't hurt overall space complexity since it's capped at k elements. 

    res = []
    
    for index in range(k):
        distance, x, y = heapq.heappop(max_heap)
        res.append([x, y])
    
    return res