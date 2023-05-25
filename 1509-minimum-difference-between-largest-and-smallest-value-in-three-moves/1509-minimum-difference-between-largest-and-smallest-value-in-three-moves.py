class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        length = len(nums) 
        
        if length <= 4:
            return 0
        nums.sort()
        
        part1 = nums[3:]
        part2= nums[:-3]
        part3 = nums[2:-1]
        part4= nums[1:-2]
        
    
        diff1 = part1[-1] - part1[0]
        diff2 = part2[-1] - part2[0]
        diff3 = part3[-1] - part3[0]
        diff4 = part4[-1] - part4[0]
      
        return min(diff1, diff2, diff3, diff4)
            
            
        
