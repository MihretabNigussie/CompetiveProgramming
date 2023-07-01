class Solution:
    def validPalindrome(self, s: str) -> bool:
        left , right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                sleft = s[left+1: right+1]
                sright = s[left: right]
                return sleft == sleft[::-1] or sright == sright[::-1]
            right -= 1
            left += 1
        return True