class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        
        def combine(idx,curr, sum_):
            prev =  1
            
            if sum_ == target:
                ans.append(curr.copy())
                return
            
            if (idx == len(candidates) or (target - sum_) < candidates[idx]):
                return
            
        
            curr.append(candidates[idx])
            
            combine(idx+1 , curr, candidates[idx]+ sum_)
            curr.pop()
            
            k=1
           
            while k+idx < len(candidates) and candidates[k+idx]==candidates[idx]:
                k += 1
            
            combine(idx + k, curr, sum_)
           

        candidates.sort()
        combine(0, [], 0)
        
        return ans
            
        