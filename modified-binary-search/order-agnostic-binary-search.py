#could be reverse sorted aka descending
#time: O(log(n)) -- binary search
#space: O(1) -- no extra aka constant
def order_agnostic_binary_search(arr, target):
    
    left = 0
    right = len(arr)-1
    
    is_ascending = arr[left] < arr[right]
    
    while left <= right:
        
        mid = (left+right)//2
        
        if arr[mid] == target:
            return mid
        
        if is_ascending:
            
            if arr[mid] < target:
                left = mid+1
            else:
                right = mid-1
        
        else:
            
            if arr[mid] < target:
                right = mid-1
            else:
                left = mid+1
    
    return -1