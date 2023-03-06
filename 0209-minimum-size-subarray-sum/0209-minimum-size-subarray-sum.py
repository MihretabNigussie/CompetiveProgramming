class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left ,right ,sum,res = 0, 0, 0, float(inf)
        flag = False
        while right < len(nums):
            sum += nums[right]
            while sum >= target:
                res = min(res, right - left + 1)
                sum -= nums[left]
                left += 1
                flag = True
            right += 1
        if not flag: return 0    
        return res