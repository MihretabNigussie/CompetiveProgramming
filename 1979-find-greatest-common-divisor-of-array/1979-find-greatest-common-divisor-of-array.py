class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        min_, max_ = min(nums) , max(nums)
        
        def gcd(num1, num2):
            if num2 == 0:
                return num1
            return gcd(num2, num1 % num2)
        
        return gcd(min_, max_)

        