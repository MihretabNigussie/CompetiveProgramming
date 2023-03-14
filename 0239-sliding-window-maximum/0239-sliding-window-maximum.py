class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = collections.deque()
        
        for i, v in enumerate(nums):
            while queue and nums[queue[-1]] < v:
                queue.pop()
            queue.append(i)
            
            if (i - k + 1) > queue[0]:
                queue.popleft()
            
            if i >= k-1:
                ans.append(nums[queue[0]])
            
        return ans
            
            
            
        
        