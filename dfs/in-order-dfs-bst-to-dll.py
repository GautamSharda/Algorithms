#in order dfs, O(n) time for visitng each node once and O(n) space 
#for internal/under the hood recursion stack
#note: LC solution slides was nice for clear understanding/picture of this
#cleaner looking solution version
def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
    if not root:
        return None
    first = None
    last = None
    def helper(node):
            
        nonlocal first, last
            
        if node:
            helper(node.left)
                
            if last:
                node.left = last
                last.right = node
                
            else:
                first = node
            last = node
            helper(node.right)
    helper(root)
    last.right = first
    first.left = last
    return first

#worse looking version, same thing though
class Solution:
    first = None
    last = None
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        self.dfs(root)
        self.last.right = self.first
        self.first.left = self.last
        return self.first
    def dfs(self, node):
            
        if node:
            self.dfs(node.left)
                
            if self.last:
                node.left = self.last
                self.last.right = node
                
            else:
                self.first = node
            self.last = node
            self.dfs(node.right)