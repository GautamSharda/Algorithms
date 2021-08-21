#look at all substrings of the input string that have len == len(pattern string)
#check if any of the substrings of the input string that have len == (pattern string) have all the characters of the pattern string, which can be done by storing each character of the pattern string in a dictionary
#to find all substrings that have the right length and then do a check, use a FIXED sliding window approach
#window of len == pattern string, then enter while loop once right size, then do check and return true
# if pass, then move window_start up

def permutations(s, p):
    
    window_start = 0
    
    for window_end in range(len(s)):
        
        while window_end-window_start+1 == len(p):
            chars = {}
            for char in p:
                if char not in chars:
                    chars[char] = 1
            is_perm = True
            for char_index in range(window_start, window_end+1):
                if s[char_index] not in chars:
                    is_perm = False
            if is_perm:
                return True
            window_start += 1
    return False
            
print(permutations("aaacb", "aaacb"))