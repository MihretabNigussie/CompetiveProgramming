# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        res = []
        left = 0
        current = head
        
        while current:
            while stack and stack[-1][0] < current.val:
                res[stack[-1][1]] = current.val
                stack.pop()
            
            stack.append((current.val, left))
            res.append(0)
            left += 1
            current = current.next
            
        return res
        
                
                
            
            
        