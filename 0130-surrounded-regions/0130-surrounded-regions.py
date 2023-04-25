class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        mySet = set()
        
        def dfs(i , j):
            
            if i >= rows or j >= cols or i <0 or j < 0 or board[i][j] == 'X' or (i,j) in mySet:
                return
            
            mySet.add((i,j))
            
            
            dfs(i, j + 1)
            dfs(i -1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            
        
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows-1 or j == 0 or j == cols-1) and board[i][j] == 'O':

                    dfs(i,j)
                    
                    
                    
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in mySet:
                    board[i][j] = 'X'
                