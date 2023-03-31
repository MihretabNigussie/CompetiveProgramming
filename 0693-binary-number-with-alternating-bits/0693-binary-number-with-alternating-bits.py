class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        bit = n & 1
        
        while n:
            n >>= 1
            
            if bit == n & 1:
                
                return False
            
            bit = n & 1
            
        return True
                
                
            
            
        