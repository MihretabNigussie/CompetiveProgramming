class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        mySet = set()
        five, ten = 0, 0
        flag = False
        
        for i in bills:
            if i == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            elif i == 5:
                five += 1
            else:
                if five >= 3 and ten == 0:
                    five -= 3
                elif five >= 1 and ten >= 1:
                    five -= 1
                    ten -= 1
                else:
                    flag = True
            if i != 20:
                mySet.add(i)
        if flag:
            return False
        return True
                
                
            
            
                
        
         
        