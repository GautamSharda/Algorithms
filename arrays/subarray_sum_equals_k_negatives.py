#nums can have negative elements, so sliding window doesn't work
#so we keep track of subarray sums in a dict 
#time = O(n)
#space = O(n)
#brute force would just be double for loop to check each subarray -- O(n^2) time, O(1) space
def subarraySum(nums):
        
    count = 0
    prefix_sums = {0:1}
    sub_sum = 0
        
    for num in nums:
            
        sub_sum += num
        
        prefix = sub_sum - k

        count += prefix_sums.get(prefix, 0)
        
        prefix_sums[sub_sum] = 1 + prefix_sums.get(sub_sum, 0)
        
    return count