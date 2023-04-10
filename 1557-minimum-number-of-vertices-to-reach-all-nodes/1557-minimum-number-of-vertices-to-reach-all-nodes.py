class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        dict = defaultdict(int)

        for v1,v2 in edges:
            dict[v2] += 1

        mySet = set() 
        
        for vertex1,vertex2 in edges:
            
            if  dict[vertex1] == 0:
                mySet.add(vertex1)
            if dict[vertex2] == 0:
                mySet.add(vertex2)

        return mySet

