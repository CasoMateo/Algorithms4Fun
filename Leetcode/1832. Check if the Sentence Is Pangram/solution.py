class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
      cur = 0 
      
      for letter in set(sentence):
        cur += 1 
      
      return cur == 26
