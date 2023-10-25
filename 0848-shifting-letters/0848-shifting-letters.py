class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        prefix = []
        currSum = 0
        for i in shifts[::-1]:
            currSum += i
            prefix.append(currSum)
        
        prefix = prefix[::-1]
       
        
        for i in range(len(s)):
           
            new_code = (((ord(s[i]) + prefix[i]) - 97) % 26) + 97
            
            s = s[:i] + chr(new_code) + s[i+1:]
        return s