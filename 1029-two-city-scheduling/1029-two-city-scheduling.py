class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        lst = []
        minCost = 0
        
        for cost in costs:
            lst.append([cost[1]- cost[0], cost[0], cost[1]])
        
        lst.sort()
        
        for i in range(len(costs)):
            if i < len(lst)/2:
                minCost += lst[i][2]
            else:
                minCost += lst[i][1]
        return minCost