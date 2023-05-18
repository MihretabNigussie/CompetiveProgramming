# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = {i+1: i+1 for i in range(size)}
        self.rank = {i+ 1 : 1 for i in range(size)}
        self.minima = {i+ 1 : inf for i in range(size)}

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y,min_):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
                self.minima[rootX] = min(self.minima[rootX],self.minima[rootY], min_ )
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
                self.minima[rootY] = min(self.minima[rootX],self.minima[rootY], min_ )
            else:
                self.root[rootY] = rootX
                self.minima[rootX] = min(self.minima[rootX],self.minima[rootY], min_ )
                self.rank[rootX] += 1
        else:
            self.minima[rootX] = min(self.minima[rootX],self.minima[rootY], min_ )
            self.minima[rootY] = min(self.minima[rootX],self.minima[rootY], min_)

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        uf = UnionFind(n)
        for i in roads:
            uf.union(i[0], i[1], i[2])
            
        num = uf.find(1)
        return uf.minima[num]
                
        
        
        