class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
       
        ans = 0
        temp = sum(arr[:k-1])
        for i in range(len(arr)-k+1):
            
            temp += arr[i + k -1]
            if temp /k >= threshold:
                ans += 1
            temp -= arr[i]
            
            
        return ans 
            