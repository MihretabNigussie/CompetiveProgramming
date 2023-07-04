class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans = 0
        mySet = set()
        left = 0
        
        for right in range(len(s)):
            
            while s[right] in mySet:
                
                mySet.remove(s[left])
                
                left += 1
            ans = max(ans, right - left + 1)
            
            mySet.add(s[right])
        return ans