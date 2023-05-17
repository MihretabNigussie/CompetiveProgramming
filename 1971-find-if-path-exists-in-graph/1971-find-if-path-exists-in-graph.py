class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        root = [i for i in range(n)]
        rank = [1]* n
        
        def find(x):
            while x != root[x]:
                x = root[x]
            return x
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    rank[rootX] += 1

        def connected(x, y):
            return find(x) == find(y)
        
        
        for i in edges:
            union(i[0], i[1])
        
        return connected(source, destination)

    