class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def combine(idx,curr, sum_):
            
            if sum_ == target:
                ans.append(curr.copy())
                return
            
            if (idx == len(candidates) or (target - sum_) < candidates[idx]):
                return
            
            
            curr.append(candidates[idx])
            combine(idx, curr, candidates[idx]+ sum_)
            curr.pop()
            combine(idx+ 1, curr, sum_)
            
        candidates.sort()
        combine(0, [], 0)
        
        return ans
            
            
            
            
            