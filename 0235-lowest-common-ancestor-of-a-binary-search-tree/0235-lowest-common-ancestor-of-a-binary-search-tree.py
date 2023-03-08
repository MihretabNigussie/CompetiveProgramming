# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # iteratively
        # current = root
        # while current:
        #     if current.val < p.val and current.val < q.val:
        #         current = current.rigth
        #     elif current.val > p.val and current.val > q.val:
        #         current = current.left
        #     else:
        #         return current

        # recursively
        if not root:
            return root
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p ,q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p ,q)
        return root
            
        