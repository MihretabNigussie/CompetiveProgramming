class Solution:
    def findComplement(self, num: int) -> int:
        
        ans = 0
        mask = 1
        l = 0
        while mask < num:
            byte = num ^ mask
            ans |= ((byte >> l) & 1) << l
            l += 1
            mask <<= 1
        return ans
        