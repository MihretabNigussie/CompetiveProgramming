# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = {i+1: i+1 for i in range(size)}
        self.rank = {i+ 1 : i for i in range(size)}

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        uf = UnionFind(len(edges))
        ans = []
        
        for i in edges:
            
            if uf.connected(i[0], i[1]):
                ans = [i[0], i[1]]
            uf.union(i[0], i[1])
            
        return ans
        