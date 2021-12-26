#cyclic sort solution -- O(n) time, O(1) space
def solution0(arr):
    i = 0
    while i < len(arr):
        j = arr[i]
        if arr[i] < len(arr) and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    for i in range(len(arr)):
        if i != arr[i]:
            return i

print(solution0([8, 3, 5, 2, 4, 6, 0, 1]))

#tim sort solution -- O(n*log(n)) time, O(n) space
def solution(arr):
    arr.sort()
    for i in range(len(arr)):
        if i != arr[i]:
            return i
print(solution([8, 3, 5, 2, 4, 6, 0, 1]))

#sum solution -- O(n) time, O(1) space
def solution2(arr):
    reg_sum = 0
    for i in range(len(arr)+1):
        reg_sum += i
    
    arr_sum = 0
    for i in range(len(arr)):
        arr_sum += arr[i]
    
    return reg_sum - arr_sum

arr = [8, 3, 5, 2, 4, 6, 0, 1]
print(solution2(arr))