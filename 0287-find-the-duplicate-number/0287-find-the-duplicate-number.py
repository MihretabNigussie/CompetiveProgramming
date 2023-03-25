class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        lenght = len(nums)
        p = 0
        while p < lenght:
            temp = nums[p] - 1

            if nums[temp] == nums[p]:
                p += 1
            else:
                nums[temp], nums[p] = nums[p] , nums[temp]
    
        for i in range(lenght):
            if nums[i] != i + 1:
                res =  nums[i]
                break
        return res
           