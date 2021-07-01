class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
     
      cur = sub = 0 
      
      if not s: return True
      
      for i in range(len(t)):
        if t[i] == s[cur]:
          sub += 1 
          cur += 1 
          
          if sub == len(s):
            return True
        
        elif t[i] == s[0]:
          sub = 1
          cur = 1 

      return False
