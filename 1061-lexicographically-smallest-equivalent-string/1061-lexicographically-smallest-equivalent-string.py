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
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        length = len(s1)
        uf = UnionFind(length)
        
        for i in range(length):
            uf.union(s1[i], s2[i])
            
        lst = []
        
        for i in baseStr:
            lst.append(uf.find(i))
        return ''.join(lst)
            