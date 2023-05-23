# UnionFind class
class UnionFind:
    def __init__(self, s):
        self.connections = {i:i for i in range(len(s))}
        self.size = {i:1 for i in range(len(s))}

    def find(self, x):
        parent = self.connections[x]
        
        while parent != self.connections[parent]:
            parent = self.connections[parent]
            
        while x != self.connections[x]:
            nextConnections = self.connections[x]
            self.connections[x] = parent
            x = nextConnections
            
        return x
    
    def union(self, x, y):
        xrep, yrep = self.find(x), self.find(y)
        if xrep != yrep:
            if self.size[xrep] > self.size[yrep]:
                self.connections[yrep] = xrep
                self.size[xrep] += self.size[yrep]
            
            else:
                self.connections[xrep] = yrep
                self.size[yrep] += self.size[xrep]

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        uf = UnionFind(points)
        
        def manDis(i1, i2, j1, j2):
            return abs(i1 - j1) + abs(i2 - j2)
        
        sums = 0
        turn = len(points)-1
        lst = []
        
        
        for i in range(len(points)):
            for j in range(len(points)):
                temp = manDis(points[i][0], points[i][1], points[j][0], points[j][1])
                heapq.heappush(lst, (temp, i, j))
        
        while turn > 0:
            num = heapq.heappop(lst)
            if not uf.connected(num[1], num[2]):
                sums += num[0]
                uf.union(num[1], num[2])
                turn -= 1
                               
        return sums
            
            
            
        
             
            
            
            
            
            
            
            
            
        
        
        
        