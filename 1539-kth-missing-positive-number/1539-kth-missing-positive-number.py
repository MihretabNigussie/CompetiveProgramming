class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        left, right  = -1 , len(arr) 

        while left + 1 < right:
            
            mid = left + (right- left)// 2
            
            if arr[mid] - mid - 1 < k:
                left = mid
            else:
                right = mid
                
        return left + k+ 1