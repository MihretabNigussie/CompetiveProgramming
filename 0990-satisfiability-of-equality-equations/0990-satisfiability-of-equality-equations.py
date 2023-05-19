# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = {chr(97 + i): chr(97 + i) for i in range(27)}

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if rootX < rootY:
                self.root[rootY] = rootX
            else:
                self.root[rootX] = rootY

    def connected(self, x, y):
        return self.find(x) == self.find(y)


    
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        uf = UnionFind(len(equations))
        
        for i in equations:
            if i[1] == '=':
                uf.union(i[0] , i[3])
        
        for i in equations:
            if i[1] == '!':
                if uf.connected(i[0], i[3]):
                    return False
        return True
        
        