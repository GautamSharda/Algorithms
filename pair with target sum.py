def solution(arr, target):
    
    left = 0
    right = len(arr)-1
    
    while left < right:
        
        sum = arr[left] + arr[right]
        
        if sum < target:
            left += 1
        
        if sum > target:
            right -= 1
        
        else:
            return [left, right]
            
print(solution([2,5,9,11], 11))