class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        lst = s.split()
        if len(pattern) != len(lst):
            return False
        
        dict1 = {}
        dict2 = {}
        
        
        for i in range(len(pattern)):
            if pattern[i] in dict1 and dict1[pattern[i]]  != lst[i]:
                return False
            dict1[pattern[i]] = lst[i]
            if lst[i] in dict2 and dict2[lst[i]] != pattern[i]:
                return False
            
            
            dict2[lst[i]] = pattern[i]
            
        return True
        
        