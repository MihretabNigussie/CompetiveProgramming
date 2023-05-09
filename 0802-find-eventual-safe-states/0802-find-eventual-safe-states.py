class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def topSort(node, colors, graph, order):
          
            if colors[node] == 1:
                return False
            
            colors[node] = 1
            
            for neighbor in graph[node]:
                if colors[neighbor] == 2:
                    continue
                    
                if not topSort(neighbor, colors, graph, order):
                    return False
            
            colors[node] = 2
            order.append(node)
            
            return True
        
        colors = [0 for _ in range(len(graph))]
        order = []
        
        for node in range(len(graph)):
            
            if colors[node] != 0:
                continue
            topSort(node, colors, graph, order)
            
        return sorted(order)
