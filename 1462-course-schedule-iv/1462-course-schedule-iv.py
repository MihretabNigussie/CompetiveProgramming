class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        incoming = [0 for _ in range(numCourses)]
        queue = deque()
        dict = defaultdict(set)
        lst = []
        
        for i, j in prerequisites:
            graph[j].append(i)
            incoming[i] += 1
        
        for i in range(numCourses):
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
        for i, j in queries:
            lst.append(j in dict[i])
        return lst
            
        
        
        
        