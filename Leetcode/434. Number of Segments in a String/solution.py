class Solution:
    def countSegments(self, s: str) -> int:
      
      tot = 0
      cur = False
      
      for i in range(len(s)):
        if s[i] != ' ':
          cur = True 
        
        else: 
          if cur: 
            tot += 1 
          cur = False 
      
      if cur: 
        tot += 1 
        
      return tot
