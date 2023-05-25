class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        
        ans = 1
        arr[0] = 1
        
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] >= 1:
                arr[i] = ans + 1
                ans += 1
        return ans