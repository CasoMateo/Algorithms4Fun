class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
      
      consistent = 0
      pool = set(allowed)
    
      for word in words:
        cur = set(word)
        if cur.issubset(pool):
          consistent += 1 
          
      return consistent
        
