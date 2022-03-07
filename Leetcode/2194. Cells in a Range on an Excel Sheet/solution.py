class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        
        
        cur = ord(s[0])
        cells = []

        while cur <= ord(s[-2]): 
            for i in range(int(s[1]), int(s[-1]) + 1):
                cells.append(chr(cur) + str(i))
            
            cur += 1 
        
        return cells
            
    
