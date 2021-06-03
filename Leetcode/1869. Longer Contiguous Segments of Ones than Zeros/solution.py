class Solution:
    def checkZeroOnes(self, s: str) -> bool:
      if len(s) == 1: 
        return True if s[0] == '1' else False
      
      max_0 = max_1 = 0 
      cur = 0
      
      for i in range(1, len(s)):
        if s[i - 1] == '0':
          if s[i - 1] == s[i]:
            cur += 1 
            max_0 = max(cur, max_0)
          else: 
            cur = 1
        else: 
          cur = 0
      
      cur = 0 
      for j in range(1, len(s)):
        if s[j - 1] == '1':
          if s[j - 1] == s[j]:
            cur += 1 
            max_1 = max(cur, max_1)
          else: 
            cur = 1
        else: 
          cur = 0 
      
      return True if max_1 > max_0 else False
      
        
