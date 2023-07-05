class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        temp = 0
        dict = defaultdict(int)
        ans = 0
        for i in range(len(nums)):
            if nums[i] % 2:
                nums[i] = 1
            else:
                nums[i] = 0
            temp += nums[i]
            dict[temp] += 1
            
            if temp == k:
                ans += 1
            ans += dict[temp - k] 

        return ans
            
        
            
        
        
        