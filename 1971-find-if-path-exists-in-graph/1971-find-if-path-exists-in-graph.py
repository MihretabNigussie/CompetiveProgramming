class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        queue = deque()
        visited = set()
        
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        queue.append(source)
        visited.add(source)
        while queue:
            
            node = queue.popleft()
            
            visited.add(node)
            if node == destination:
                return True
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
            
        return False
            
            
        