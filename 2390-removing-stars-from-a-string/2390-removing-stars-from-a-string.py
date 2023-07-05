class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = []
        ans = ''
        for i in s:
            if i != '*':
                stack.append(i)
                
            else:
                stack.pop()
        for i in stack:
            ans += i
        return ans
                
                