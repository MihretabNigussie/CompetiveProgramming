class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        def findDistance(x1,y1,x2,y2):
            return math.sqrt((x2-x1)**2 + (y2-y1)**2)
        
        graph = defaultdict(list)
        
        ans = 0
        
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                distance = findDistance(bombs[i][0], bombs[i][1], bombs[j][0], bombs[j][1])
                
                if distance <= bombs[i][2]:
                    
                    graph[i].append(j)
   
                
        def dfs_recursive(graph, start):
            
            visited.add(start)

            for neighbor in graph[start]:
                if neighbor not in visited:
                    dfs_recursive(graph, neighbor)
    
            return visited
        
        for node in graph:
                visited = set()
                dfs_recursive(graph, node)
                ans = max(len(visited), ans)
        return ans
                
                    
                    
        