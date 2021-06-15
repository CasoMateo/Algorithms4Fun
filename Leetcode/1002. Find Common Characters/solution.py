class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        res = []
        
        for letter in words[0]:
          common = True
          for j in range(1, len(words)):
            if letter not in words[j]:
              common = False
            else:
              words[j] = words[j].replace(letter, '', 1)
              
          if common:
            res.append(letter)
      
        return res
