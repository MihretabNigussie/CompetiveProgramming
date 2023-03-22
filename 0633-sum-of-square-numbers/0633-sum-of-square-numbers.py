class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        n = int(math.sqrt(c))
        
        left, right = 1 , n
        
        if c == 0:
                return True
        
        while left <= right:
            if left ** 2 == c or right ** 2 == c:
                return True
            num = (left ** 2) + (right ** 2)
            if num > c:
                right -= 1
            elif num < c:
                left += 1
            else:
                return True
        return False
        