class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj=[[] for _ in range(n+1)]
        
        for i ,j,w in times:
            adj[i].append((j,w))
            
        dst=[float("infinity")]*(n+1)
        dst[0]=0
        dst[k]=0
        st=[]
        heapq.heapify(st)
        
        for i,w in adj[k]:
            dst[i]=w
            heapq.heappush(st,(w,i))
            
        while st:
           
            wt,x=heapq.heappop(st)
            for i,w in adj[x]:
                if wt+w<dst[i]:
                    dst[i]=wt+w
                    heapq.heappush(st,(wt+w,i))
                    
       
        if float("infinity") in dst:
            return -1
        return max(dst)
