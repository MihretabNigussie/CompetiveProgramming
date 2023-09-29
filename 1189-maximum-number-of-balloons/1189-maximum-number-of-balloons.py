class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        dict1 = Counter(text)
        dict2 = Counter('balloon')
        count = inf
        
        for char in dict2:
            if char in dict1:
                if dict1[char] < dict2[char]:
                    return 0
                if char == 'l' or char == 'o':
                    count = min(count , dict1[char]//2)
                else:
                
                    count = min(count , dict1[char])
            else:
                return 0
        return count
        