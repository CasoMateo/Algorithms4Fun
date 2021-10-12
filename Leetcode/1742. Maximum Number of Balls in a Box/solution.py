class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        mem = {}
        
        for i in range(lowLimit, highLimit + 1):
          cur = 0
          
          for j in str(i):
            cur += int(j) 
          
          mem[cur] = mem.get(cur, 0) + 1
        
        largest = 0 
        
        for freq in mem: 
          largest = max(largest, mem[freq])
        
        return largest
