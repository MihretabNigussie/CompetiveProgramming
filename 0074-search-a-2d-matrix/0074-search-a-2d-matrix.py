class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        finalRow = []
        flag = True
        
        for row in matrix:
            if row[-1] >= target:
                finalRow = row
                flag = False
                break
        if flag:
            return False
        
        left , right = -1, len(finalRow)
        
        while left + 1 < right:
            mid = left + (right - left)//2
            
            if target < finalRow[mid]:
                right = mid
            elif target > finalRow[mid]:
                left = mid
            else:
                return True
        return False
        
                
        
                
        
        
        