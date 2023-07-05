class Solution:
    def isValid(self, s: str) -> bool:
        
        dict = {
            ')': '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []
        
        for i in s:
            
            if i in dict.keys():
                if not stack or stack[-1] != dict[i]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
            
        if stack:
            return False
        return True
        