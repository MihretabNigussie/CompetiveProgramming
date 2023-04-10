class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        dict = defaultdict(list)

        for v1,v2 in roads:
            dict[v2].append(v1)
            dict[v1].append(v2)
        max_ = 0
        
        for i in dict.keys():
            temp = 0
 
            for j in dict.keys():
                if i != j:
                    temp = len(dict[i]) + len(dict[j])
                if i in dict[j]:
                    temp -= 1
                max_ = max(max_, temp)
        return max_
        
            
                    