class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
      
      pat = self.rationalize(pattern)
      equal = []
      
      for i in range(len(words)):
       
        if self.rationalize(words[i]) == pat:
          equal.append(words[i])
      
      return equal
          
    def rationalize(self, word):
      
      mem = {} 
      cur = 0 
      word = list(word)
      
      for j in range(len(word)):
        if word[j] not in mem: 
          cur += 1
          mem[word[j]] = chr(cur + 97)
        
        word[j] = mem[word[j]]
          
      return ''.join(word)
          
