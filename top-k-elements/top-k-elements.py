#time = O(N∗logK)
#space = O(k)

from heapq import *

def solution(arr, k):
    
    min_heap = []
    
    for i in range(k):
        
        heappush(min_heap, arr[i])
    
    for i in range(k, len(arr)):
        
        if arr[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, arr[i])
    
    return min_heap
    
print(solution([3, 1, 5, 12, 2, 11], 3))