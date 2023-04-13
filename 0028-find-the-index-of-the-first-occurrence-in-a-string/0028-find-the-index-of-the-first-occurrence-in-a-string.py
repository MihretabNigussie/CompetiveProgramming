class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        p1, p2 = 0, len(needle)-1
        length = len(haystack)-1
        
        while p2 <= length:
            if haystack[p1:p2+1] == needle:
                return p1
            p1 += 1
            p2 += 1
        return -1