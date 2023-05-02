class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(x1,x2):
            return -sqrt(x1 ** 2 + x2 **2)
        
        lst = []
        for i, v in enumerate(points):
            lst.append((distance(v[0], v[1]), i))
        
        
        heapq.heapify(lst)
        
        
        while len(lst) > k:
            heapq.heappop(lst)

        ans = []
        
        for i in lst:
            ans.append(points[i[1]])
        return ans
            
        
        