class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        return self.remaining(s) == self.remaining(t)
    
    def remaining(self, s):
      
      rem = []
        
      for i in range(len(s)):
        if s[i] == '#':
          if rem: 
            rem.pop()
            
        else: 
          rem.append(s[i])
      
      return rem
            
