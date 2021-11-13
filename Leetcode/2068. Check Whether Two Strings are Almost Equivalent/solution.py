from collections import Counter

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
      
      mem1 = self.frequencies(word1)
      mem2 = self.frequencies(word2)
      
      largest = max(self.differences(mem1, mem2), self.differences(mem2, mem1))
                
      return largest <= 3
    
    def frequencies(self, string):
      
      mem = {}
      
      for char in string: 
        mem[char] = mem.get(char, 0) + 1
      
      return mem
    
    def differences(self, mem1, mem2):
      
      actual = 0 
      
      for char in mem1:
        if char not in mem2:
          cur = mem1[char]
        
        else:
          cur = abs(mem1[char] - mem2[char])
        
        actual = max(actual, cur)
      
      return actual
