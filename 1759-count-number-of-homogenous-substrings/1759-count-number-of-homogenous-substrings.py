class Solution:
    def countHomogenous(self, s: str) -> int:
        
        left = 0
        count = 0
        s += ' '
        
        for right in range(len(s)):
            
            temp = 0
            
            if s[left] != s[right]:
                
                for i in range(1, right - left + 1):
                    
                    temp += i
            
                count += temp
                left = right
        return count % (10**9 + 7)
                
                