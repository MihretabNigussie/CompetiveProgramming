# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        dict = {}
        max_ = -1
        
        
        def traverse(root):
            
            nonlocal max_
            
            
            if not root:
                return 0
            
            leftSum = traverse(root.left)
            rightSum = traverse(root.right)
            
            tempAns = leftSum + rightSum + root.val
            
            dict[tempAns] = dict.get(tempAns, 0) + 1
            
            if max_ < dict[tempAns]:
                max_ =  max(max_ , dict[tempAns])
            
            return leftSum + rightSum + root.val
        
            
        traverse(root)
        
        lst2= []
        
        for key in dict.keys():
            if dict[key] == max_:
                lst2.append(key)
        
        return lst2
        