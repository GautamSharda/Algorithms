#bottom up dp with dp array as cache for memoization
#Time complexity: O(N), n is number of elements in the input array
#Space complexity: O(N), space is required for the memo array


def houseRobber(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    else:
        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            dp.append(max(nums[i]+dp[i-2], dp[i-1]))
    return dp[len(dp)-1]
