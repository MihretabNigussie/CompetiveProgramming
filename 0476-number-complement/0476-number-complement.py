class Solution:
    def findComplement(self, num: int) -> int:
        
        ans = 0
        l = 0
        while num:
            bit = (num & 1) ^ 1
            ans |= bit << l
            l += 1
            num >>= 1
        return ans
            
        
        # ans = 0
        # mask = 1
        # l = 0
        # while mask < num:
        #     byte = num ^ mask
        #     ans |= ((byte >> l) & 1) << l
        #     l += 1
        #     mask <<= 1
        # return ans
        