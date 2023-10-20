class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        lst = [1] * length
        prefix = 1
        for i in range(length):
            
            lst[i] *= prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(length -1, -1, -1):
            
            lst[i] *= postfix
            postfix *= nums[i]
        return lst
            