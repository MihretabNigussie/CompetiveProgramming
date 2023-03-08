# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        count = {}
        def vertical(root, row = 0, col= 0):
            nonlocal count
            if not root:
                return 
            if col not in count:
                count[col] = []
            count[col].append((row, root.val))

            vertical(root.left, row + 1, col - 1)
            vertical(root.right, row + 1, col + 1)

        vertical(root)
        ans = []
        for n in sorted(count.keys()):
            count[n].sort()
            for i in range(len(count[n])):
                count[n][i] = count[n][i][1]
            ans.append(count[n])
            
        return ans
    
    
