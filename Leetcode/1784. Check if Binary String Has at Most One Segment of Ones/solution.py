class Solution:
    def checkOnesSegment(self, s: str) -> bool:
    
      cur = False
      ones = 0
      
      for i in range(len(s)):
        if s[i] == '0':
          if cur: 
            ones += 1 
            
          cur = False 
        
        else: 
          cur = True
 
      if cur: ones += 1

      return ones == 1
