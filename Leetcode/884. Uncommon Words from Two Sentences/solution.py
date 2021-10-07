from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
      
      mem1 = Counter(s1.split(' '))
      mem2 = Counter(s2.split(' '))
      
      uncommon = []
      
      for freq in mem1: 
        if mem1[freq] == 1 and freq not in mem2:
          uncommon.append(freq)
      
      for freq in mem2: 
        if mem2[freq] == 1 and freq not in mem1:
          uncommon.append(freq)
      
      return uncommon
    
          
