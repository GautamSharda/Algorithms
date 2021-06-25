#sliding window problem
#use a hashmap to track frequency of characters in the window
#start by increasing the size of the window until the number of distinct characters is equal(?) to k
#then measure the size of the window and add another character, repeat until number of distinct characters is greater than k
#then shrink window by removing the first character until size of window is equal to k...


#Input: String="araaci", K=2
#Output: 4

def solution (string, k):
    
    window_start = 0
    window = {}
    highest_substring_len = 0
    
    for window_end in range(len(string)):
        
        if string[window_end] in window:
            window[string[window_end]] += 1
        
        else:
            window[string[window_end]] = 1

        while len(window) > k:
            window[string[window_start]] -= 1
            if window[string[window_start]] == 0:
                del window[string[window_start]]
            window_start += 1

        highest_substring_len = max(highest_substring_len, window_end - window_start + 1)
    
    return highest_substring_len

print(solution("cbbebi", 3))
#^^ prints 5, which is correct

#Time Complexity 
#O(N) where ‘N’ is the number of characters in the input string. 
#The outer for loop runs for all characters and the inner while loop processes each character only once, so T(N) = (N+N) which is asymptotically equivalent to O(N).

#Space Complexity 
#The space complexity of the algorithm is O(K), as we will be storing a maximum of ‘K+1’ characters in the HashMap.
