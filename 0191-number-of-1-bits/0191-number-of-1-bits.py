class Solution:
    def hammingWeight(self, n: int) -> int:
        
        counter = 0
        
        while n:
            counter += n % 2
            
            n >>= 1
        return counter
        
        
        # more efficient
#         counter = 0
        
#         while n:
            # counteres += 1
#         return res