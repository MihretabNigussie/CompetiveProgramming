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
       
        
        lst = []
        for i, v in enumerate(nums):
            if nums[i] != i+1:
                lst.append(nums[i])
            if i+1 != v:
                lst.append(i+1)
                return lst