class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        lst = []
        
        for i in nums:
            lst.append(sorted(nums).index(i))
        
        return lst
            
        
        
        