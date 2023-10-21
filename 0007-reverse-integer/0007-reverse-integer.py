class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x = abs(x)  

        revs_number = 0

        while x > 0:
            remainder = x % 10
            revs_number = (revs_number * 10) + remainder
            x = x // 10

        if is_negative:
            revs_number = -revs_number  
            
        if revs_number > ( 2**31 )-1 or revs_number < -2 ** 31:
            
            return 0
        return revs_number