class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        new_word = ''
        number = 1
        
        for i in range(len(sentence)):
        
          if sentence[i] == ' ':
            if self.is_prefix(new_word, searchWord):
              return number
            number += 1
            new_word = ''
          elif i == len(sentence) - 1:
      
            new_word += sentence[i]
            if self.is_prefix(new_word, searchWord):
              return number
          else:
            new_word += sentence[i]
        
        return -1
    
    def is_prefix(self, word, searchWord):
      
      if len(searchWord) > len(word):
        return False
      for i in range(min(len(searchWord), len(word))):
        if searchWord[i] != word[i]:
          return False 
      return True 
