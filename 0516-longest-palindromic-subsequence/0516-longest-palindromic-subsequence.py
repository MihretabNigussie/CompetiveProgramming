class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        text1 = s
        text2 = s[::-1]
        
        @cache
        def dp(idx1,idx2):
            
            if idx1 == len(text1) or idx2 == len(text2):
                return 0

            if text1[idx1] == text2[idx2]:
                return dp(idx1+1,idx2+1) + 1
            else:
                return max(dp(idx1+1,idx2),dp(idx1,idx2+1))

        return dp(0,0)