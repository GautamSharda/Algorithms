#medium
#time = O(n^2)
#space = O(n)
def threeSum(nums):
    triplets = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i] != nums[i-1]:
            self.two_sum(nums, i, triplets)
    return triplets
        
def two_sum(nums, target_index, triplets):
    target = -nums[target_index]
    left = target_index+1
    right = len(nums)-1
    while left < right:
        curr_sum = nums[left]+nums[right]
        if curr_sum < target:
            left+=1
        elif curr_sum > target:
            right-=1
        else:
            triplets.append([-target, nums[left], nums[right]])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left-1]:
                left+=1
