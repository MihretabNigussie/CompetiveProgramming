class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not s or (len(s) < len(t)): 
            return ''
        
        countT , window = {} , {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have, need = 0, len(countT)
        left = 0
        res , resLen = [-1, -1], float('inf')
        
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if char in countT and countT[char] == window[char]:
                have += 1
            
            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
            
        left, right = res 
        return s[left: right + 1] if resLen < float("inf") else ''
            
            