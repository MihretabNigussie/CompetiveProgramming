class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        monstersTime = []
        count = 0
        for i in range(len(dist)):
            monstersTime.append(math.ceil(dist[i]/speed[i]))
        
        monstersTime.sort()
        
        for i in range(len(monstersTime)):
            
            if i >= monstersTime[i]:
                return count
            count += 1
            
        return count
        