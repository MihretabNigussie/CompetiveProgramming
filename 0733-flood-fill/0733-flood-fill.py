class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        
        temp = image[sr][sc]
        
        def dfs(i , j):
            nonlocal temp
            
            if i >= len(image) or j >= len(image[0]) or i <0 or j < 0 or image[i][j] != temp or image[i][j] == color:
                return
            
                
            image[i][j] = color

            dfs(i, j + 1)
            dfs(i -1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)

            return 
        
        dfs(sr, sc)
        image[sr][sc] = color
        return image
            
        
        