# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # lst = []
        # while head:
        #     lst.append(head.val)
        #     head = head.next
        # left, right = 0, len(lst)-1
        # while left <= right:
        #     if lst[left] != lst[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True
        
        # Follow up
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True