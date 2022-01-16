#medium
#Time = O(n)
#Space = O(n)
def minRemoveToMakeValid(s):
    #remove any close before open
    #remove any open after end
    stack = []
    skip_these = set()
    result = []
    for i in range(len(s)):
        if not stack:
            if s[i] == ')':
                skip_these.add(i)
                i-=1
            elif s[i] == '(':
                stack.append(i)
        else:
            if s[i] == ')':
                stack.pop()
            elif s[i] == '(':
                stack.append(i)
    skip_these = skip_these.union(set(stack))
    for j in range(len(s)):
        if j not in skip_these:
            result.append(s[j])
    return ''.join(result)