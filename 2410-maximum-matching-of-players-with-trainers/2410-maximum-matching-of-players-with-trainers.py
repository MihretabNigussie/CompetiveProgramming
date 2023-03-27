class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        counter = 0
        
        players.sort()
        trainers.sort()
        
        left , right = 0, 0
        
        while left < len(players) and right < len(trainers):
            
            if players[left] <= trainers[right]:
                counter += 1
                left += 1
                right += 1
            else:
                right += 1
        return counter
        