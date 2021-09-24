from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
      
      mem = Counter(magazine)
      
      for i in range(len(ransomNote)):
        
        if ransomNote[i] not in mem: 
          return False 
      
        else: 
          if mem[ransomNote[i]] == 0: 
            return False 
          mem[ransomNote[i]] -= 1 
      
      return True
