class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        delta = [0] * 101
        conversionDiff = 1950
        
        for log in logs:
            
            delta[log[0] - conversionDiff] += 1
            delta[log[1] - conversionDiff] -= 1
        
        tempSum = 0
        maxPopulation = 0
        year = 1950
        
        for i, v in enumerate(delta):
            
            tempSum += v
            
            if tempSum > maxPopulation:
                maxPopulation = tempSum
                year = conversionDiff + i
        return year