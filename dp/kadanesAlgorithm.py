import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum = 0
        max_sum = -math.inf
        
        for i in range(len(nums)):
            
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        
        return max_sum