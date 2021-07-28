from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
      
      freqS = Counter(s)
      freqT = Counter(t)
      operations = 0
      
      for char in freqT:
   
        if char not in freqS:
          operations += freqT[char]
                 
        elif freqT[char] > freqS[char]:
          operations += abs(freqT[char] - freqS[char])

      return operations
      
      
    
    
      
        
