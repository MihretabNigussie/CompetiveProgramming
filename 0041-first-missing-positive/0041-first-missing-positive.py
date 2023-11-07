class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        ans = 1
        for i in nums:
            if i > 0:
                if ans == i:
                    ans += 1
                elif ans < i:
                    return ans
        return ans