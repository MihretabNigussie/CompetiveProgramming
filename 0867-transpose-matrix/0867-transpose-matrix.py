class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row,column=len(matrix),len(matrix[0])
        res=[[0 for _ in range(row)] for _ in range(column)]
        for i in range(row):
            for j in range(column):
                res[j][i]=matrix[i][j]
        return res