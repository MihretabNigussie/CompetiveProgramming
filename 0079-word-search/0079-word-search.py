class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board) , len(board[0])
        path = set()
        
        def helper(row, col, i):
            if i == len(word):
                return True
            if ((row < 0) or (col < 0) or 
            (row >= rows) or (col >= cols)
            or (word[i]  != board[row][col]) or
            ((row, col) in path)):
                return False
            
            path.add((row, col))
            
            res = (helper(row + 1, col, i+1) or
            helper(row-1, col, i+1) or
            helper(row, col + 1, i + 1) or
            helper(row, col - 1, i + 1) )
            
            path.remove((row, col))
            return res
        for row in range(rows):
            for col in range(cols):
                if helper(row, col, 0):
                    return True
        return False
                