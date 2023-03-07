# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1 and not root2:
            return None
        if root1:
            v1 = root1.val
        else:
            v1 = 0
            
        if root2:
            v2 = root2.val
        else:
            v2 = 0
        
        root3 = TreeNode(v1 + v2)
        
        if root1 and root2:
            root3.left = self.mergeTrees(root1.left , root2.left)
        elif not root1:
            root3.left = self.mergeTrees(None, root2.left)
        else:
            root3.left = self.mergeTrees(root1.left, None)
            
            
        if root1 and root2:
            root3.right = self.mergeTrees(root1.right , root2.right)
        elif not root1:
            root3.right = self.mergeTrees(None, root2.right)
        else:
            root3.right = self.mergeTrees(root1.right, None)
        
        return root3