class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        lst = []
        
        for i in range(n+1):
            if i == 0 or i == 1:
                lst.append(i)
            elif i % 2 == 0:
                lst.append(lst[i//2])
            else:
                lst.append(lst[i//2] + lst[i//2 + 1])
        return max(lst)
        