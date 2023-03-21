class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(flag):
            left , right = -1, len(nums)
            temp = -1
            while left + 1 < right:
                mid = left + (right - left) // 2

                if nums[mid] > target:
                    right = mid
                elif nums[mid] < target:
                    left = mid
                else:
                    temp = mid
                    if flag:
                        right = mid
                    else:
                        left = mid
            return temp
        
        left = binarySearch(True)
        right = binarySearch(False)
        return [left, right]
                
        