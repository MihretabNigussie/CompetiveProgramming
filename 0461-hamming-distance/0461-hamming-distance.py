class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        counter = 0
        
        while x or y:
            xNum = x % 2
            yNum = y % 2
            
            if xNum != yNum:
                counter += 1
                
            x >>= 1
            y >>= 1
        return counter
        