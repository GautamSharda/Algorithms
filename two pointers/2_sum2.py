#time: O(n)
#space: O(1)
def twoSum(numbers):
    left = 0
    right = len(numbers)-1
    while left < right:
        curr_sum = numbers[left]+numbers[right]
        if curr_sum < target:
            left += 1
        elif curr_sum > target:
            right -= 1
        else:
            return [left+1, right+1]