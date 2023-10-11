class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        currDir = 'N'
        currPos = [0,0]
        
        direction = {'N': [0, 1], 'S': [0, -1], 'W': [-1, 0], 'E': [1, 0]}
        
        changeDir = {
            'N' : {'L': 'W', 'R': 'E'},
            'S' : {'L': 'E', 'R': 'W'},
            'W' : {'L': 'S', 'R': 'N'},
            'E' : {'L': 'N', 'R': 'S'}
        }
        
        for instruction in instructions:
            
            if instruction == 'G':
                
                currPos[0] += direction[currDir][0]
                currPos[1] += direction[currDir][1]
                
            else:
                currDir = changeDir[currDir][instruction]
        
        if currDir != 'N' or currPos == [0,0]:
            return True
        return False