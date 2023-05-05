# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)
        for index,head in enumerate(lists):
            if head:
                 heapq.heappush(heap, (head.val,index, head))
        dummy = cur = ListNode(0)
        while heap:
            num ,index, node = heapq.heappop(heap)
            cur.next = node
            cur  = node
            if cur.next:
                heapq.heappush(heap,(cur.next.val ,index, cur.next))
        
        return dummy.next
            