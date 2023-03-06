class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = -inf
        left = 0 
        runningSum = 0
        for right in range(len(nums)):
            runningSum += nums[right]
            if right - left + 1 == k:
                temp = runningSum / k
                runningSum -= nums[left]
                avg = max(avg, temp) 
                left += 1
        return avg
            
            