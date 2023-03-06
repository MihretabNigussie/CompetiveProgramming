class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst = []
        sum = 0
        for i in nums:
            sum += i
            lst.append(sum)
        return lst
