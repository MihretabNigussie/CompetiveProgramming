class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        
        for eq, val in zip(equations, values):
            a, b = eq
            graph[a].append([b, val])
            graph[b].append([a, 1/val])
        
        def bfs(src, target):
            if src not in graph or target not in graph:
                return -1
            queue, visited = deque(), set()
            
            queue.append([src, 1])
            visited.add(src)
            
            while queue:
                
                node, weight = queue.popleft()
                
                if node == target:
                    return weight 
                    
                
                for newNode, newWeight in graph[node]:
                    
                    if newNode not in visited:
                        queue.append([newNode, weight * newWeight ])
                        visited.add(newNode)
            return -1
        return [bfs(query[0], query[1]) for query in queries ]
                    