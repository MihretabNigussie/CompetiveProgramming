class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        rows, cols = len(grid), len(grid[0])
        area = 0
        
        def dfs(i , j):
            
            if (i,j) in visited or i >= rows or j >= cols or i <0 or j < 0 or grid[i][j] == 0:
                return 0
            
            visited.add((i,j))

            return 1 +  dfs(i, j + 1) + dfs(i -1, j) + dfs(i + 1, j) + dfs(i, j - 1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] :
                    area = max(area ,dfs(i,j))
        return area
        