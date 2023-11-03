class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict = {}
        
        for i , v in enumerate(nums):
        
            temp = target - v
            
            if v in dict:
                
                return [i, dict[v]]
            
            dict[temp] = i
        