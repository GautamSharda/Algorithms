import math
# time, space = O(n), O(n)
def validate(self, root, lower=-math.inf, upper=math.inf):
           
    if not root:
        return True
            
    if root.val <= lower or root.val >= upper:
        return False
            
    return self.validate(root.left, lower, root.val) and self.validate(root.right, root.val, upper)
    
def isValidBST(self, root: Optional[TreeNode]) -> bool:   
    return self.validate(root)