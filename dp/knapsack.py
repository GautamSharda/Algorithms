#Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C’. Each item can only be selected once, which means either we put an item in the knapsack or we skip it.

#Weights: { 2, 3, 1, 4 }
#Profits: { 4, 5, 3, 7 }
#Capacity = 5
#dp = array of lengths items containing arrays of length capacity
def solution(weights, profits, capacity):
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return recur(dp, weights, profits, capacity, 0)

def recur(dp, weights, profits, capacity, index):
    
    if index >= len(profits) or capacity-weights[index] < 0:
        return 0
    
    if dp[index][capacity] != -1:
        return dp[index][capacity] 
    
    else:
        inclusive_max_profit = profits[index]+recur(dp, weights, profits, capacity-weights[index], index+1)
        exclusive_max_profit = recur(dp, weights, profits, capacity, index+1)
        dp[index][capacity] = max(inclusive_max_profit, exclusive_max_profit)
        return dp[index][capacity]

print(solution([2,3,1,4], [4,5,3,7], 5))