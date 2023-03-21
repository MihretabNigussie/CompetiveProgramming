class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
         
        
        maxSum = sum(weights)
        left , right = max(weights) -1, maxSum + 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            res = 1
            currSum = 0
            for i in weights:
                if currSum + i > mid:
                    res += 1
                    currSum = 0
                
                currSum += i

            if res > days:
                left = mid
            elif res <= days:
                right = mid
        return right
            
                
                
            
                
        
        