class Solution:
    def arrangeCoins(self, n: int) -> int:
        left , right = 1 , n
        res = 0
        while left <= right:
            mid = left + (right - left)//2
            coins = mid/2 * (mid+1)
            if coins <= n:
                left = mid + 1
                res = max(res, mid)
            else:
                right = mid -1
        return res
        