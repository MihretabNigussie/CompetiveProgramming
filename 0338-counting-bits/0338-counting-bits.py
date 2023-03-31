class Solution:
    def countBits(self, n: int) -> List[int]:
        
        lst = []
        
        for i in range(n+1):
            counter = 0
            while i :
                counter += i & 1
                    
                i >>= 1
            lst.append(counter)
        return lst
                    
        