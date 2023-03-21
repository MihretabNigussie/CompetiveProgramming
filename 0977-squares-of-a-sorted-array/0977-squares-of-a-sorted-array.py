class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # lst = []
        # left , right = 0, len(nums)-1
        # while (left <= right):
        #     if nums[left] ** 2 > nums[right] ** 2:
        #         lst.append(nums[left]**2)
        #         left += 1
        #     else:
        #         lst.append(nums[right] ** 2)
        #         right -= 1
        # return lst[::-1]    `
        
        lst = []
        for i in nums:
            lst.append(i**2)
        lst.sort()
        return lst