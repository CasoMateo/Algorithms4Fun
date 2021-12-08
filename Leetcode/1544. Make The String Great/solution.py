class Solution:
    def makeGood(self, s: str) -> str:
      
      cur = 0

      while cur < len(s) - 1:
        
        if (s[cur].lower() == s[cur] and s[cur].upper() == s[cur + 1]) or (s[cur].upper() == s[cur] and s[cur].lower() == s[cur + 1]):
          s = s[: cur] + s[cur + 2: ]
          
          if cur > 0: 
            cur -= 1 
          continue
            
        cur += 1
      
      return s
