class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        count = 0
        visited = set()
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]:
                    graph[i].append(j)

        def dfs_recursive(graph, start):
            
            visited.add(start)

            for neighbor in graph[start]:
                if neighbor not in visited:
                    dfs_recursive(graph, neighbor)
            return visited

        for node in graph:
            if node not in visited:
                count += 1
                dfs_recursive(graph, node)
        return count

                    
        