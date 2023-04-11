# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        
        def dfs(node):   
            
            if not node.left and not node.right:
                return '(' + str(node.val) + ')'
            
            left, right = '', ''
            
            if node.left:
                left = dfs(node.left)
                
            if node.right:
                right = dfs(node.right)
            
            if right and not left:
                left = '()'
            
            return '(' + str(node.val)  + left + right+ ')'
                
        return dfs(root)[1:-1]
        
