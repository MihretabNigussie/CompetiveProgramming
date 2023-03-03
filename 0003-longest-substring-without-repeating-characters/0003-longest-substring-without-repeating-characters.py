class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        mySet = set()
        res = 0
        for right in range(len(s)):
            while s[right] in mySet:
                mySet.remove(s[left])
                left +=1
            mySet.add(s[right])
            res = max(res, right - left +1)
        return res

