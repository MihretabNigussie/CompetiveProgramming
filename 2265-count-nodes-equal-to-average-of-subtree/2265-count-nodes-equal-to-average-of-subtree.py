# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        result = 0
		
        def traverse(root):
            nonlocal result
            
            if not root:
                return 0, 0
            
            left_sum, left_count = traverse(root.left)
            right_sum, right_count = traverse(root.right)
            
            total_sum = root.val + left_sum + right_sum
            total_count = 1 + left_count + right_count
            
            if total_sum // total_count == root.val:
                result += 1
            
            return total_sum, total_count
        
        traverse(root)
        
        return result