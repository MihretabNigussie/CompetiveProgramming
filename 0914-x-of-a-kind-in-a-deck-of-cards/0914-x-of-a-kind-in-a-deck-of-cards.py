class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
      
        
        def gcd(num1, num2):
            if num2 == 0:
                return num1
            return gcd(num2, num1 % num2)
        
        dict = Counter(deck)
        
        lst =list(dict.values())
        
        if len(lst) == 1:
            return lst[0] > 1
            
        curr =  lst[0]
        for i in range(len(lst)):
            curr = gcd(curr,lst[i])
            
        
            
        return curr > 1
        