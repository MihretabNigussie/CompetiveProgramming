class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        if not n % 2:
            return n
        k = n
        while k % 2:
            
            k *= 2
        
        return k