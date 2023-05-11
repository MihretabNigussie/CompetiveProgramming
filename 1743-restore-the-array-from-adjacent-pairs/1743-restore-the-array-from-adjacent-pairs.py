class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        lst1 = []
        graph = defaultdict(list)
        queue = deque()
        visited = set()
        ans = []
        
        for i in adjacentPairs:
            lst1.append(i[0])
            lst1.append(i[1])
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
            
        dict = Counter(lst1)
    
        for i in dict:
            if dict[i] == 1:
                queue.append(i)
                break
                
        while queue:
            num = queue.popleft()
            ans.append(num)
            visited.add(num)
            
            for neighbour in graph[num]:
                
                if neighbour not in visited:
                    queue.append(neighbour)
        return ans
                    
                    
                
        