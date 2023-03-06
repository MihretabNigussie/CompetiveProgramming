class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        n = len(arr)
        k = k % n                 
# Here reminder is taken because if we had 10 rotation but our array is of size 9 then only 1 rotation is effective to produce ans.

        arr[n - k:] = arr[n - k:][::-1]  
        arr[:n - k] = arr[:n - k][::-1]
        arr[:] = arr[::-1]             