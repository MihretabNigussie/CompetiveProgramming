class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        incoming = [0 for _ in range(n)]
        queue = deque()
        dict = defaultdict(set)
        lst = [[] for _ in range(n)]
        
        for i in edges:
            graph[i[0]].append(i[1])
            incoming[i[1]] += 1
        
        for i in range(n):
            if incoming[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            
            for neighbour in graph[node]:
                incoming[neighbour] -= 1
                dict[neighbour].add(node)
                
                if dict[node]:
                    dict[neighbour].update(dict[node])
                
                if incoming[neighbour] == 0:
                    queue.append(neighbour)
        
        for i in dict:
            lst[i] = sorted(list(dict[i]))
            
        return lst
                
        
        
        
        
            
        
        
        