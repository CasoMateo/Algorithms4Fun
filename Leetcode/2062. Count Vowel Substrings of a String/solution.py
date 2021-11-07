class Solution:
    def countVowelSubstrings(self, word: str) -> int:
      
      vowel = 0 
      
      for i in range(len(word)):
        for j in range(i + 1, len(word)):
          cur = word[i: j + 1]
          
          if set(cur) == set(['a', 'e', 'i', 'o', 'u']):
            vowel += 1 
            
      return vowel
      
        
        
