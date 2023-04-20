class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # using bit manipulation
        ans, curr = [], []
        
        used = 0
        
        def build(i = 0):
            nonlocal used 
            if i == len(nums):
                ans.append(curr.copy())
                return 
            
            for idx, num in enumerate(nums):
                if (used & (1 << idx)== 0):
                    used |= 1 << idx
                    curr.append(num)
                    build(i+1)
                    curr.pop()
                    used ^= 1 << idx
        build()
        return ans
                    
        # using backtracking
        # result = []
        
#         # base case
#         if len(nums) == 1:
#             return [[nums[0]]]
        
#         for _ in range(len(nums)):
#             n = nums.pop(0)
#             perms = self.permute(nums)
            
#             for perm in perms:
#                 perm.append(n)
#             result.extend(perms)
#             nums.append(n)
#         return result


        