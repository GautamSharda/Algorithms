#O(n) time (probably)
#O(1) space
#This solution is mind blowing. The idea is to say p to root is length  a + c and q to root is length b + c where c is the length of the lca to root. Then we are just making p and q travel the same distance a + b + c by the "swapping when root" trick. So they exactly meet at that common merging point which is the LCA.

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        p1, p2 = p, q
        
        while p1!=p2:
            
            if p1.parent:
                p1 = p1.parent
            else:
                p1 = q
            
            if p2.parent:
                p2 = p2.parent
            else:
                p2 = p
                
        return p1