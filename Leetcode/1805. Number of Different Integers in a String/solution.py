class Solution:
    def numDifferentIntegers(self, word: str) -> int:
      
      digits = set()
      cur = ''
      
      for i in range(len(word)):
        if word[i].isdigit():
          cur += word[i]
        
        else: 
          if len(cur) > 0: 
            digits.add(int(cur))
            cur = ''
      
      if len(cur) > 0: 
        digits.add(int(cur))
      
      return len(digits)
