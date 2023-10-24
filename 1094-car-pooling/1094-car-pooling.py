class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        passChange = [0] * 1001
        
        for trip in trips:
            
            passenger, start, end = trip
            passChange[start] += passenger
            passChange[end] -= passenger
         
        currPassenger = 0
        for i in range(1001):
            
            currPassenger += passChange[i]
            
            if currPassenger >  capacity:
                return False
        
        return True
            