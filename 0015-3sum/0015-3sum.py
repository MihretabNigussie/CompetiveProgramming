class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while(left < right):
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif nums[i] + nums[left] + nums[right]> 0:
                    right -= 1
                else:
                    left += 1
        return res
