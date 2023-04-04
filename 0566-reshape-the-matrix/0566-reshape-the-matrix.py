class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        rows, cols  = len(mat), len(mat[0])
        
        if rows * cols != r * c:
            return mat
        
        ans = []
        lst = []
        
        for row in range(rows):
            for col in range(cols):
                ans.append(mat[row][col])
                
        p,l = 0,0
  
        for i in range(r):
            temp = ans[l:l+c]
            lst.append(temp)
            l += c 

            
        return lst
        