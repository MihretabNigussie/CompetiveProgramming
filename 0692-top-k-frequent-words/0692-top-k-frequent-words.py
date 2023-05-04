class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        dict = Counter(words)
       
        maxHeap = [(-dict[count], count) for count in dict.keys()]
        heapq.heapify(maxHeap)
        count = 0
        lst = []
        
        while count < k:
            lst.append(heapq.heappop(maxHeap)[1])
            count += 1
        
        return lst
            
         