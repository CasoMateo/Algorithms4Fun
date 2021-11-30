class Solution:
    def makeFancyString(self, s: str) -> str:
      
      fancy = []
      cur = 0
      prev = ''
      
      for i in range(len(s)):
        if s[i] == prev: 
          cur += 1 
          
          if cur >= 2:
            continue
        
        else: 
          cur = 0
        
        fancy.append(s[i])
        prev = s[i]
        
      return ''.join(fancy)
