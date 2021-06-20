#increase size of window until it is greater than or equal to s, then update smallest_window_so_far, decrease size of window until it is not greater than or equal to s, then repeat

#Input: [2, 1, 5, 2, 3, 2], S=7 
#Output: 2

import math

def solution(arr, s):
    window_start = 0
    smallest_window_so_far = math.inf
    window_sum = 0
    
    for window_end in range(len(arr)):
        
        window_sum += arr[window_end]

        while window_sum >= s:
            smallest_window_so_far = min(window_end-window_start+1, smallest_window_so_far)
            window_sum -= arr[window_start]
            window_start += 1
    
    if smallest_window_so_far == math.inf:
        return 0
    
    return smallest_window_so_far
    

print(solution([3, 4, 1, 1, 6], 100 ))