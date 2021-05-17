class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
      mem = {}
      m = c = 0
      
      if len(s) <= 2: 
        return 0
      
      for i in range(len(s)):
        if s[i] in mem:
          c = i - mem[s[i]] - 1
          m = max(c, m)
        else: 
          mem[s[i]] = i 
      
      if m == 0: 
        return -1 
    
      return m 
          
    
