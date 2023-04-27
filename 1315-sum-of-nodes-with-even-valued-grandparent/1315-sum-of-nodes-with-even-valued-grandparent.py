# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        sum_ = 0
        
        def dfs(node, parent, gParent):
            nonlocal sum_
            
            if not node:
                return 
            
            if gParent % 2 == 0:
                sum_ += node.val
            
            dfs(node.left,node.val,parent)
            dfs(node.right,node.val,parent)
            
            return 
        dfs(root, -1, -1)
        return sum_