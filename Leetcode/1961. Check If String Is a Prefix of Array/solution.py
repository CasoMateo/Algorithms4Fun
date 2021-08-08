class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
      
      accum = [] 
      
      for i in range(len(words)):
        accum.append(words[i])
        
        if ''.join(accum) == s:
          return True 
      
      return False
