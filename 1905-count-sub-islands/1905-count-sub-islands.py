class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid1), len(grid1[0])
        count = 0
        
        def dfs(i , j):
            
            if (i,j) in visited or i >= rows or j >= cols or i <0 or j < 0 or grid2[i][j] == 0:
                return True
            
            visited.add((i,j))
            flag = True
            
            if grid1[i][j] == 0:
                flag = False
                
            flag = dfs(i, j+1)   and flag
            flag = dfs(i -1, j) and flag 
            flag = dfs(i + 1, j) and flag
            flag = dfs(i, j - 1) and flag
            
            return flag

        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] and (i,j) not in visited and dfs(i,j):
                    count += 1
        return count
        
        