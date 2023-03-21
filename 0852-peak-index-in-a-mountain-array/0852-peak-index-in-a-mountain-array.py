class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        left , right = -1 , len(arr)

        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if arr[mid-1] < arr[mid] and arr[mid + 1] < arr[mid]:
                return mid
            
            if arr[mid] < arr[mid + 1]:
                left = mid
            elif arr[mid - 1] > arr[mid]:
                right = mid
            
         
        
        

        