#understand, match, plan, implement, review, evaluate

#understand: input = root node of a binary tree 
#(at most 2 children nodes), sum that a path must add up to

#match: depth first search b/c a valid path is defined from root-leaf

#root, recursive algorithm, check if current node is None, if yes,
#return false
#seed value to start with, check if it's the
#base case, leaf is equal to s, if leaf and if yes, then return true, if no 
#then subtract node.val from sum, and recur for both children
#increment to find a path

validPaths = 0

class treeNode:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


def allPaths(node, s):

    if node == None:
        return 0
    
    if node.right==None and node.left==None and node-s == 0:
        return 1
    
    else:
        s = s - node
        validPaths += allPaths(node.left, s) + allPaths(node.right, s)
    
    return validPaths

def main():
    root = treeNode(1)
    root.left = treeNode(7)
    root.right = treeNode(9)
    root.left.left = treeNode(4)
    root.left.right = treeNode(5)
    root.right.left = treeNode(2)
    root.right.right = treeNode(7)

    allPaths(root, 12)

main()

