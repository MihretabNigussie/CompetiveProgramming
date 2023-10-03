class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        string = ''
        
        for digit in digits:
            string += str(digit)
        
        temp = str(int(string) + 1)
        
        return [int(temp[i]) for i in range(len(temp))]