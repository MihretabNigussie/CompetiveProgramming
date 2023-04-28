"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        dict = {}
        graph = defaultdict(list)
        visited = set()
        
        for i in employees:
            dict[i.id] = i.importance
            graph[i.id].append(i.subordinates)
        
        sum_ = 0
        
        def dfs_recursive(graph, start):
            nonlocal sum_
            
            visited.add(start)
            sum_ += dict[start]

            for neighbor in graph[start][0]:
                if neighbor not in visited:
                    dfs_recursive(graph, neighbor)
            return
        for i in employees:
            if i.id == id:
                dfs_recursive(graph, i.id)
                break
        return sum_

        