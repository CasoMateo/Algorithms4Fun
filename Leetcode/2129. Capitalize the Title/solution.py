class Solution:
    def capitalizeTitle(self, title: str) -> str:
      words = title.split(' ')
      
      capitalized = []
      
      for word in words: 
        if len(word) > 2: 
          cur = word[0].upper() + word[1: ].lower()
        
        else: 
          cur = word.lower()
        
        capitalized.append(cur)
      
      return ' '.join(capitalized)
