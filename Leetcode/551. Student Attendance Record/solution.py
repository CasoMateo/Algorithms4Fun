class Solution:
    def checkRecord(self, s: str) -> bool:
    
      longest = cur = 0 
      
      for i in range(len(s)):
        if s[i] == 'L':
          cur += 1 
        
        else: 
          longest = max(longest, cur)
          cur = 0 
      
      longest = max(longest, cur)
      
      if s.count('A') < 2 and longest < 3:
        return True
      return False
