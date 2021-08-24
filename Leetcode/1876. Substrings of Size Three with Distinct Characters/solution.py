class Solution:
    def countGoodSubstrings(self, s: str) -> int:
      
      if len(s) < 3: 
        return 0 
      
      good = 0 
      for i in range(3, len(s) + 1):
        
        if len(set(s[i - 3 : i])) == len(s[i - 3 : i]):
          good += 1 
      
      return good
