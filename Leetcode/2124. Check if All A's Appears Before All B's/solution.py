class Solution:
    def checkString(self, s: str) -> bool:
      
      ending = -1
      
      for i in range(len(s)):
        if s[len(s) - i - 1] == 'a':
          ending = len(s) - i - 1
          break
          
      initial = len(s) 
      
      for j in range(len(s)):
        if s[j] == 'b': 
          initial = j 
          break
          
      return ending < initial 
