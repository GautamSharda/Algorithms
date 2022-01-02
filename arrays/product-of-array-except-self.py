#medium
#product except self = product of stuff to left * product of stuff to right
#product of stuff to left/right = curr_element*prev_product_of_stuff
#calculate product of stuff to left and put in answer array
#then calculate product of stuff to right and multiply with stuff to left in answer array
#return answer list
#time = O(n)
#space = O(1) -- answer array is "given" as part of the problem, but otherwise it'd obvi be O(n)
def productExceptSelf(nums):
    answer = [0]*len(nums)
    answer[0] = 1
    for i in range(1, len(nums)):
        answer[i] = answer[i-1]*nums[i-1]
    r = 1
    for i in reversed(range(len(nums))):
        answer[i] *= r
        r *= nums[i]
    return answer

print(productExceptSelf([1,2,3,4]))