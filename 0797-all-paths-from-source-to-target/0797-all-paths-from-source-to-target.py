class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        visited = set()
        max_  = len(graph) - 1
       
        def all_paths(graph, start, end, path=[]):
            path = path + [start]
            
            if start == end:
                return [path]
        
            paths = []
            
            for node in graph[start]:
                
                if node not in path:
                    new_paths = all_paths(graph, node, end, path)
                    
                    for p in new_paths:
                        paths.append(p)
            return paths

        
        return all_paths(graph, 0, max_)
        
       
            
        