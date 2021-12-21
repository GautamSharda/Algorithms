#Difficulty = Medium
#Solution = Sort intervals by start time, iterate, merge along the way
#Time = timsort + one iteration = N*log(N) + N = O(N*log(N))
#Space = timsort + output list = N + N = O(N)
def solution(intervals):
    
    intervals.sort(key=lambda i:i[0])
    
    output = [intervals[0]]
    global_start = output[0][0]
    global_end = output[0][1]
    
    for i in range(1, len(intervals)):
        curr_start = intervals[i][0]
        curr_end = intervals[i][1]
        if curr_start <= global_end:
            global_end = max(global_end, curr_end)
            output[-1][1] = global_end
        else:
            output.append(intervals[i])
            global_start = curr_start
            global_end = curr_end
    return output

print(solution([[1,4], [2,6], [3,5]]))
