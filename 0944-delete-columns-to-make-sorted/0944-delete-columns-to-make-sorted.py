class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        ans = 0
        lst = [i for i in strs[0]]
        mySet = set(i for i in range(len(strs[0])))
        
        for i in range(len(strs)):
            for j in range(len(strs[0])):
                
                if j  in mySet:
                    if strs[i][j] < lst[j]:
                        ans += 1
                        mySet.remove(j)
                    lst[j] = strs[i][j]
                
        return ans
    
        
    