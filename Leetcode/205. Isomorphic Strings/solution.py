
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
      
      mapping = {}
      
      for i in range(len(s)):
        if t[i] not in mapping.values() and s[i] not in mapping: 
          mapping[s[i]] = t[i]
    
      for j in range(len(t)):
        if s[j] not in mapping or t[j] != mapping[s[j]]:
          return False 
      
      return True

      
