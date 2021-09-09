class Solution(object):
    def containsDuplicate(self, nums):
        
        #Sorting => time = O(n*Log(n)), space = O(1)
        #nums.sort()
        #for i in range(len(nums)-1):
        #    if nums[i] == nums[i+1]:
        #        return True
        #return False
        
        #Use dictionary + DP => time = O(n), space = O(n)
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return True
            else:
                d[nums[i]] = i
        return False