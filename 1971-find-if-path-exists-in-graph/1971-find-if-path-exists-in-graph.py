class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def validPath(edges):
            graph = defaultdict(list)
            
            for edge in edges:
                
                graph[edge[0]].append(edge[1])
                graph[edge[1]].append(edge[0])

            return graph
        
        visited = set()
        
        def dfs(graph , node, visited, destination):
            if node == destination:
                return True
            visited.add(node)
 
            for neighbour in graph[node]:
                if neighbour not in visited:
        
                    found = dfs(graph,neighbour, visited,destination)
                    if found:
                        return True
                    
            return False
        
        return dfs(validPath(edges),source,set(), destination )
            
            
                