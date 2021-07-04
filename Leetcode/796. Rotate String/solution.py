class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
      
      if not s and not goal: 
        return True
    
      for char in s:
        s = s.replace(char, '', 1)
        s += char
          
        if s == goal: return True 
        
      return False
