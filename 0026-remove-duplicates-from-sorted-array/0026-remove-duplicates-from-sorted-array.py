class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left , right = 0, 1
        for right in range(len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        return left + 1