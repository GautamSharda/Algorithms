class treeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def hasSum(root, s):
    
    if (current.left==None and current.right==None):
        if (s = root):
            return True
        else:
            return False
    
    else:
        s = s - root #9, 7,  
        hasSum(s, root.left)
        hasSum(s, root.right)

def main():

    root = treeNode(1)
    root.left = treeNode(2)
    root.right = treeNode(3)
    root.left.left = treeNode(4)
    root.left.right = treeNode(5)
    root.right.left = treeNode(6)
    root.right.right = treeNode(7)

    hasSum(root, 10)

main()