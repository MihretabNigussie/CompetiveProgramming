# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            curr_level_size = len(queue)
            curr = []
            
            for _ in range(curr_level_size):
                node = queue.popleft()
                curr.append(node.val)
                
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)
            
            result.append(curr)
        
        return result[::-1]