class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        
        sCount , pCount = {}, Counter(p)

        
        for i in range(len(p)):
            sCount[s[i]] = sCount.get(s[i], 0) + 1
            
            
        if sCount == pCount:
            res = [0]
        else:
            res = []
        
        left = 0
        
        for right in range(len(p), len(s)):
            sCount[s[right]] = sCount.get(s[right], 0) + 1
            sCount[s[left]] -= 1
            
            if sCount[s[left]] == 0:
                sCount.pop(s[left])
            left += 1
            
            if sCount == pCount:
                res.append(left)
        return res
            
        
            
        