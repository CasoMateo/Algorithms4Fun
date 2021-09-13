class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
      
      if ch not in word:
        return word 
      
      new = []
      
      for i in range(word.index(ch) + 1):
        new.append(word[word.index(ch) - i])
        
      return ''.join(new) + word[word.index(ch) + 1: ]
