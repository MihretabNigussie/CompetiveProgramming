class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        rows, cols  = len(mat), len(mat[0])
        
        if rows * cols != r * c:
            return mat
        
        ans = []
        lst = []
        r_ , c_ = 0, 0
        for row in range(rows):
            for col in range(cols):
                ans.append(mat[row][col])
        # print(ans)
        p = 0
        l = 0
        for i in range(r):
            temp = ans[l:l+c]
            # print(temp)
            lst.append(temp)
            l += c 
        # print(lst)
            
        return lst
        