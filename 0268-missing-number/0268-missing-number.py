class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        p = 0
        while p < len(nums):

            if p != (nums[p]) and nums[p] < len(nums):
                num = nums[p]
                nums[num] , nums[p] = nums[p], nums[num]
            else:
                p += 1
        

        for i, v in enumerate(nums):
            if i != v:
                return i
        return len(nums) 
        