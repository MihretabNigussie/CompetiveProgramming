class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        for i in range(len(matrix[0])-1):
            prev = matrix[0][i]
            
            row , col = 1, i+1
            while row < len(matrix) and col < len(matrix[0]):
                if matrix[row][col] != prev:
                    return False
                prev = matrix[row][col]
                row += 1
                col += 1
        
        for i in range(len(matrix)-1):
            prev = matrix[i][0]
            
            row , col = i + 1, 1
            while row < len(matrix) and col < len(matrix[0]):
                if matrix[row][col] != prev:
                    return False
                prev = matrix[row][col]
                row += 1
                col += 1
        
            
            
        return True
        