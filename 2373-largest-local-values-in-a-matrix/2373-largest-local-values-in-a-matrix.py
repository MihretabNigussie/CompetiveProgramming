class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        length= len(grid)

        ans = [[0] * (length - 2) for _ in range(length - 2)]

        for i in range(length - 2):
            
            for j in range(length - 2):
                
                for k in range(3):
                    
                    for l in range(3):
                        
                        ans[i][j] = max(ans[i][j], grid[i + k][j + l])
        return ans
        