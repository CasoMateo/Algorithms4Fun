from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
      mem1 = Counter(words1)
      mem2 = Counter(words2)
      
      words1.extend(words2)
      ocs = 0
      
      for word in set(words1):
        if word not in mem1 or word not in mem2:
          continue 
        
        if mem1[word] == 1 and mem2[word] == 1:
          ocs += 1
 
      return ocs
      
