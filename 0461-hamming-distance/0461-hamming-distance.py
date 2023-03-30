class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        counter = 0
        
        while x or y:
            xNum = x & 1
            yNum = y & 1
            
            if xNum != yNum:
                counter += 1
                
            x >>= 1
            y >>= 1
        return counter
        