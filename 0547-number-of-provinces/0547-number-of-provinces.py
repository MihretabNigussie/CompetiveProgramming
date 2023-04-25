class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        count = 0
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]:
                    graph[i].append(j)
    
        
        def dfs_recursive_disconnected(graph):
            nonlocal count
            visited = set()
            for start in graph:
                if start not in visited:
                    count += 1
                    dfs_recursive_helper(graph, start, visited)
 
        def dfs_recursive_helper(graph, start, visited):
            visited.add(start)
            for neighbor in graph[start]:
                if neighbor not in visited:
                    dfs_recursive_helper(graph, neighbor, visited)

        
        dfs_recursive_disconnected(graph)
        return count
        
