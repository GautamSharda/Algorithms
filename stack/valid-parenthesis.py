def isValid(s):
    #Keep track of last open brackets seen -- stack -- and match with closing brackets -- key-value pairs aka hashmap aka dict.
    #Time = O(n)
    #Space = O(n)
    opened_stack = []
    closed_pairs = {')':'(', ']':'[', '}':'{'}
    for i in range(len(s)):
        if s[i] in closed_pairs:
            if not opened_stack or closed_pairs[s[i]] != opened_stack.pop():
                return False
        else:
            opened_stack.append(s[i])
    return False if opened_stack else True

print(isValid('([]){}([)]'))