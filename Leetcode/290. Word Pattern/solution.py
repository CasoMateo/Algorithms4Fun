class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split(' ')
        
        if len(words) != len(pattern):
          return False
    
        mapping = {}
        
        for j in range(len(words)):
          
          if words[j] not in mapping:
            if pattern[j] in mapping.values(): 
              return False
            mapping[words[j]] = pattern[j]
          
          words[j] = mapping[words[j]]

        return words == list(pattern)
          
        
        
          
          
        
        
          
