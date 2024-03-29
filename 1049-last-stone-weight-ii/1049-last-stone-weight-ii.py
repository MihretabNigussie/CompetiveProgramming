class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        total = sum(stones)

        @cache
        def dp(i,summ):
            if i == len(stones):
                return abs(summ - (total -summ ))
            take = dp(i+1,summ+stones[i])
            not_take = dp(i+1,summ)

            return min(take,not_take)

        return dp(0,0)