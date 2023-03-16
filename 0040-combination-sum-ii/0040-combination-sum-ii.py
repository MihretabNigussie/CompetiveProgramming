class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        
        def combine(idx,curr, sum_):
            prev =  -1
            
            if sum_ == target:
                ans.append(curr.copy())
                return
            
            if (idx == len(candidates) or (target - sum_) < candidates[idx]):
                return
            
            for i in range(idx ,len(candidates)):
                if prev == candidates[i]:
                    continue
                curr.append(candidates[i])
                combine(i + 1 , curr, candidates[i]+ sum_)
                curr.pop()
                prev = candidates[i]

        candidates.sort()
        combine(0, [], 0)
        
        return ans
            
        