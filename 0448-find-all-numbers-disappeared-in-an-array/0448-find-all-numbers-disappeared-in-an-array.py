class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        lenght = len(nums)
        p = 0
        while p < lenght:
            temp = nums[p] - 1

            if nums[temp] == nums[p]:
                p += 1
            else:
                nums[temp], nums[p] = nums[p] , nums[temp]
       
        res = []
        for i in range(lenght):
            if nums[i] != i + 1:
                res.append(i+1)
            i += 1
        return res



        