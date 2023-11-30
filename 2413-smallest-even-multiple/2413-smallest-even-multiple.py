class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        if not n % 2:
            return n
        
        while n % 2:
            
            n *= 2
        
        return n