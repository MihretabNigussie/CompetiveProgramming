class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        heap = []

        # Push elements along with their indices sum onto the heap
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                # Use the sum of indices as a sorting key
                heapq.heappush(heap, (i + j, j, nums[i][j]))
        
        # Pop elements from the heap to get the sorted diagonal order
        diagonal_order = []
        while heap:
            diagonal_order.append(heapq.heappop(heap)[2])
        
        return diagonal_order