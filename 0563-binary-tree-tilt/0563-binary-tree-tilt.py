# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        tilt = []
        
        def traverse(root):
            
            
            if not root:
                return 0
            
            leftSum = traverse(root.left)
            rightSum = traverse(root.right)
            
            tilt.append(abs(leftSum - rightSum))
            
            return leftSum + rightSum + root.val
            
        traverse(root)
        
        return sum(tilt)
        
        
        
        