class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        lenght = len(nums)
        p = 0
        while p < lenght:
            temp = nums[p] - 1

            if nums[temp] == nums[p]:
                p += 1
            else:
                nums[temp], nums[p] = nums[p] , nums[temp]
       
        
        for i, v in enumerate(nums):
            
            if i+1 != v:
                return [v, i+1]