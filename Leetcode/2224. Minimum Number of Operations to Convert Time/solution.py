class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        if current == correct: 
            return 0
        
        hours1, minutes1 = current.split(':')
        hours2, minutes2 = correct.split(':') 
        pos = [60, 15, 5, 1]
        dif = ((int(hours2) * 60 + int(minutes2)) - (int(hours1) * 60 + int(minutes1))) 
        moves = 0 
        
        while dif != 0: 
            for cur in pos: 
               if cur <= dif: 
                 dif -= cur 
                 break 
              
            moves += 1 
        
        return moves
