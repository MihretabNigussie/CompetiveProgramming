class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        k = len(nums) -k
        
        def quickSort(left, right):
            pivot ,pointer = nums[right] , left
            
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[pointer] , nums[i] = nums[i] , nums[pointer]
                    pointer += 1
            nums[pointer] , nums[right] = nums[right] , nums[pointer]
            
            if pointer > k:
                return quickSort(left, pointer - 1)
            elif pointer < k:
                return quickSort(pointer + 1, right)
            else:
                return nums[pointer]
        return quickSort(0, len(nums)-1)
        