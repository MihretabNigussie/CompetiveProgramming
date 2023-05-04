class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        count = 0
        
        while count < k:
            pile= heapq.heappop(piles)
            
            heapq.heappush(piles, floor(pile/2))
            count += 1
            
        return abs(sum(piles))
            
            
        
        
        