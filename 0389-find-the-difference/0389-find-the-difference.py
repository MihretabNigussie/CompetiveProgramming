class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        dict1 = Counter(s)
        dict2 = Counter(t)
       
        
        for key in dict2.keys():
            
            if key not in dict1.keys():
                return key
            if dict1[key] != dict2[key]:
                return key