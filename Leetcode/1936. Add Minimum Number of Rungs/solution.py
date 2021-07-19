class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
    
      cur = needed = i = 0 
        
      for i in range(len(rungs)):
        if rungs[i] - cur > dist: 
          needed += (rungs[i] - cur - 1) // dist
        cur = rungs[i]
          
      return needed
        
