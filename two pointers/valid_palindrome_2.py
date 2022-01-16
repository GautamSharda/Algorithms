#Time = O(n)
#Space = O(1)
def validPalindrome(s):
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            return self.isPalindrome(s, left+1, right) or self.isPalindrome(s, left, right-1)
        else:
            left += 1
            right -= 1
    return True
def isPalindrome(s, left, right):
    while left <= right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True