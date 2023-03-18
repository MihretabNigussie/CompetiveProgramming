# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        lst = []
        
        def traversal(root):
            
            if not root:
                return 
            
            lst.append(root.val)
            traversal(root.left)
            traversal(root.right)
            
        traversal(root)
        
        return lst
                
        