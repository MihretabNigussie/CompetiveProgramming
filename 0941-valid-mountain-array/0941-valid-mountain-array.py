class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        n = len(arr)
        if n < 3:
            return False
        
        curr = 0
        while curr < n -1 and  arr[curr] < arr[curr + 1]:
            curr += 1
        if curr == 0 or curr == n - 1:
            return False

        while curr < n- 1 and arr[curr] > arr[curr + 1]:
            curr += 1
        if curr == n - 1:
            return True
        
        return False