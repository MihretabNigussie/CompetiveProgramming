class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        if n == 0:
            return 1
        
        ans = 0
        mask = 1
        l = 0
        while mask < n:
            byte = n ^ mask
            ans |= ((byte >> l) & 1) << l
            l += 1
            mask <<= 1
        return ans