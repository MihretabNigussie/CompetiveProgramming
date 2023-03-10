# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
         # base case
        if not head or not head.next:
            return head
        
        left = head
        slow, fast = head , head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow
    
        temp = right.next
        right.next= None
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)
        
        tail = node = ListNode(0)
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left:
            tail.next = left
        if right:
            tail.next = right
        return node.next

       
        
        

   



       