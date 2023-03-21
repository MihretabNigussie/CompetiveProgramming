class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        counter = 0
        
        for i in range(len(strs[0])):
            current = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] < current:
                    counter += 1
                    break
                else:
                    current = strs[j][i]

        return counter
                
        