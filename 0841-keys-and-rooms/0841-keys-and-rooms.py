class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        queue = deque()
        queue.append(0)
        visited = set([0])
        
        
        while queue:
            
            size = len(queue)
            
            node = queue.popleft()
            
            for child in rooms[node]:
                if child not in visited:
                    queue.append(child)
                    visited.add(child)
        
        return len(visited) == len(rooms)
            
        
        