class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        for i in range(len(mat)):
            
            count = 0
            for j in range(len(mat[i])):
                
                if mat[i][j] == 1:
                    count += 1
                    
            mat[i] = (count , i)
        
        lst = []
        
        mat.sort(key= lambda x: x[0])
        
        return [mat[x][1] for x in range(k)]
            
            
            
            
                
                