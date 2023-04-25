class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        graph_ = defaultdict(list)
        lst =  []
        visited = set()
        max_  = len(graph) - 1
        
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i]:
                    graph_[i].append(graph[i][j])
        
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

        
        return all_paths(graph_, 0, max_)
        
       
            
        