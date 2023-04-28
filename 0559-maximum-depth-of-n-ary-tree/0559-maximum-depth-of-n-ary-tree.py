"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def max_depth(root):
            max_child_depth = 1
            
            if not root:
                return 0
            if not root.children:
                return 1
            
            for child in root.children:
                max_child_depth = max(max_child_depth, max_depth(child)) 
                
            return max_child_depth + 1

        return max_depth(root)
        