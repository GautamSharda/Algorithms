#time and space - O(max(n1, n2))
#find int representation by converting to unicode and subtracting ord('0')
#then add each digit, store sum, store carry, append each digit to a list
#lastly, traverse digit list (reverse), convert each to string, concantenate, return
def addStrings(num1, num2):
        
    res = []
    carry = 0
    
    p1 = len(num1)-1
    p2 = len(num2)-1
    
    while p1 >= 0 or p2 >= 0:
            
        if p1 >= 0:
                
            x1 = ord(num1[p1])-ord('0')
            
        else:
                
            x1 = 0
            
        if p2 >= 0:
                
            x2 = ord(num2[p2])-ord('0')
            
        else:
                
            x2 = 0
            
        this_sum = (x1+x2+carry)%10
        carry = (x1+x2+carry)//10
        res.append(this_sum)
            
        p1 -= 1
        p2 -= 1
        
    if carry:
        res.append(carry)
            
    output = ''
        
    for x in reversed(range(len(res))):
        output += str(res[x])
        
    return output