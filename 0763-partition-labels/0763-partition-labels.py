class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        dict = {}
        for i, v in enumerate(s):
            dict[v] = i
            
        lst = []
        size, lastIndex = 0, 0
        for i, v  in enumerate(s):
            lastIndex = max(lastIndex, dict[v])
            size += 1
            
            if i == lastIndex:
                lst.append(size)
                size = 0
        return lst
        