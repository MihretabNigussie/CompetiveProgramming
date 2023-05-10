class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        incoming = [0 for _ in range(numCourses)]
        queue = deque()
        order = []
        
        for i in prerequisites:
            graph[i[1]].append(i[0])
            incoming[i[0]] += 1
        
        for i in range(numCourses):
            if incoming[i] == 0:
                queue.append(i)
            
        while queue:
            course = queue.popleft()
            order.append(course)
            
            for neighbour in graph[course]:
                incoming[neighbour] -= 1
                
                if incoming[neighbour] == 0:
                    queue.append(neighbour)
                    
        if len(order) != numCourses:
            return []
        
        return order
                    
                
            
        