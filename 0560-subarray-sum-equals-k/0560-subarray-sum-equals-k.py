class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ans = 0
        temp = 0
        dict = defaultdict(int)
        
        for i in range(len(nums)):
            
            temp += nums[i]
            
            if temp == k:
                ans += 1
                
            ans += dict[temp-k]
            dict[temp] += 1

        return ans