class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
      count = 0 
      res = word
      
      while res in sequence: 
        res += word
        count += 1 
     
      return count
