class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 0, max(piles)+1
        
        while left + 1 < right:
            temp= 0
            mid = left + (right- left) // 2
            for i in piles:
                temp += math.ceil(i/mid)
                
            if temp <= h:
                right = mid
            elif temp > h:
                left = mid
            
        return right
            
        