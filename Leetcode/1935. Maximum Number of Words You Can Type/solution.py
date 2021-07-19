class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
      
      broken = 0 
      is_broken = False
      
      for char in text: 
        if char in brokenLetters: 
          is_broken = True 
        if char == ' ':
          if is_broken: 
            broken += 1 
          is_broken = False
      
      if is_broken: 
        broken += 1
      
      words = 0 
    
      for c in text: 
        if c == ' ':
          words += 1 
      words += 1 
  
      return words - broken
    
