class Solution:
    def detectCapitalUse(self, word: str) -> bool:
      
      return word == self.to_upper(word) or word == self.to_lower(word) or word == (word[0].upper() + word[1: ].lower())
      
    def to_upper(self, word):
      
      upper = []
      
      for char in word: 
        upper.append(char.upper())
      
      return ''.join(upper)
    
    def to_lower(self, word):
      
      lower = []
      
      for char in word: 
        lower.append(char.lower())
      
      return ''.join(lower)
    
    
    
      
