class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dict = Counter(words[0])
        
        
        for i in range(1, len(words)):
            dict2 = Counter(words[i])
            for k, v in dict.items():
                value = min(v, dict2.get(k, 0))
                dict[k] = value
        
        res = []
        for k, v in dict.items():
            if v: 
                res.extend( [k] * v)
        
        return res
       