class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        visited = set()
        temp = image[sr][sc]
        
        def dfs(i , j):
            nonlocal temp
            
            if (i,j) in visited or i >= len(image) or j >= len(image[0]) or i <0 or j < 0:
                return
            visited.add((i,j))
            if image[i][j] == temp:
                image[i][j] = color
                dfs(i, j + 1)
                dfs(i -1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                return 
            
            
            return image
        
        
        dfs(sr, sc)
        image[sr][sc] = color
        return image
            
        
        