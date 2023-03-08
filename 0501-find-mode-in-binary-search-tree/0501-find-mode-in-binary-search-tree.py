# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        
        def traverse(root):
            if not root:
                return

            traverse(root.left)
            lst.append(root.val)
            traverse(root.right)
            
        traverse(root)
        dict = Counter(lst)
        lst2 = []
        maxi = -1
        for key in dict.keys():
            k = dict[key]
            if maxi < k:
                maxi = max(k, maxi)
                ans = key
        for key in dict.keys():
            if dict[key] == maxi:
                lst2.append(key)
                
        return lst2
        
        
        