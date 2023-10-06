# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
       
        dict = {0:1}
        self.count = 0
        def dfs(root, currSum):
            
            if not root:
                return
            
            currSum += root.val
            self.count += dict.get(currSum - targetSum, 0)
            dict[currSum] = dict.get(currSum, 0 ) + 1
            
            dfs(root.left, currSum)
            dfs(root.right , currSum)
            
            dict[currSum] -= 1
            
        dfs(root,0)
        return self.count
