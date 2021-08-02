class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
      
      res = []
      
      if len(word1) < len(word2):
        al = word1 
      else: 
        al = word2
      
      for i in range(len(al)):
        res.append(word1[i])
        res.append(word2[i]) 
      
      if al == word1:
        remaining = word2 
      else: 
        remaining = word1 
        
      res.append(remaining[i + 1 : len(remaining)]) 
    
      return ''.join(res)
