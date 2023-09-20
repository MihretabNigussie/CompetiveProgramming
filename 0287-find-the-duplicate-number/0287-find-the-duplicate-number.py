class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        length = len(nums)
        p = 0
        while p < length:
            temp = nums[p] - 1

            if nums[temp] == nums[p]:
                p += 1
            else:
                nums[temp], nums[p] = nums[p] , nums[temp]
                
        
        for i in range(length):
            if nums[i] != i + 1:
                return nums[i]
                
           