class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
    
      cur = needed = i = 0 
    
      while i < len(rungs):
        if rungs[i] - cur <= dist: 
          cur = rungs[i]
        else: 
          needed += (rungs[i] - cur - 1) // dist 
          cur = rungs[i] 
        i += 1 
        
      return needed
        
