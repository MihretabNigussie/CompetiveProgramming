class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        left , right = 0, max(nums)
        
        while left + 1 < right:
            sum_ = 0
            
            mid = left + (right- left) // 2
            
            for i in nums:
                sum_ += math.ceil(i/mid)

                
            if sum_ <= threshold:
                right = mid
            elif sum_ > threshold:
                left = mid
           
        return right
            
        
        