class Solution:
    def hammingWeight(self, n: int) -> int:
        
        counter = 0
        mask = 1
        
        while mask <= n:
            counter += 1 if n & mask  else 0
            mask <<= 1
        return counter
        
        
        