# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dict = {}
        max_ = -1
        ans = 0
        
        def traverse(root):
            nonlocal max_
            if not root:
                return

            traverse(root.left)
            dict[root.val] = 1 + dict.get(root.val, 0)
            if max_ < dict[root.val]:
                max_ = max(max_, dict[root.val])
            
            traverse(root.right)
            
        traverse(root)
       
        lst2= []
        
        for key in dict.keys():
            if dict[key] == max_:
                lst2.append(key)
                
        return lst2
        
        
        