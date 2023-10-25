class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        
        prefix = [ 0 for _ in range(len(s) + 1)]
        
        for shift in shifts:
            
            start , end, direction = shift
            
            if direction:
                
                prefix[start] += 1
                prefix[end + 1] -= 1
            else:
                prefix[start] -= 1
                prefix[end  + 1] += 1
            
        currSum = 0
        for i in range(len(s)):
            
            currSum += prefix[i]
            new_code = (((ord(s[i]) + currSum) - 97) % 26) + 97
            
            s = s[:i] + chr(new_code) + s[i+1:]
        return s