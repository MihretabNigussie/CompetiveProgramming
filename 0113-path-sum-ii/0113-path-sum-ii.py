# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        lst = []
        
        def add(root, currSum, temp ):
            
            if not root:
                return
        
           
            currSum += root.val
            temp.append(root.val)
            
            if not root.left and not root.right and currSum == targetSum:
                lst.append(list(temp))
            
            
            add(root.left, currSum, temp)
            add(root.right , currSum , temp)
            let = temp.pop()
            currSum -= let
        add(root, 0, [])
        
        return lst
            
            