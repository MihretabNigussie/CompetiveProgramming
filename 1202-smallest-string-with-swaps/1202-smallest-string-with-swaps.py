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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        uf = UnionFind(s)
        dict = defaultdict(list)
        lst = []
        
        for i in pairs:
            uf.union(i[0], i[1])
            
        for i in range(len(s)):
            rep = uf.find(i)
            dict[rep].append(s[i])
         
        for i in dict:
            dict[i].sort()
       
        for i in range(len(s)):
            rep = uf.find(i)
            lst.append(dict[rep].pop(0))
            
        return ''.join(lst)
        
        
        
        
        
        
        
        
        
        
            
        