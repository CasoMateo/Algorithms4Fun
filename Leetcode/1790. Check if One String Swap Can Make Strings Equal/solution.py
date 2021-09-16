class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        if s1 == s2: 
          return True 
        
        pairs = []
        
        for i in range(len(s1)):
          if s1[i] != s2[i]:
            pairs.append((s1[i], s2[i]))
          
          if len(pairs) > 2:
            return False
        
        return len(pairs) == 2 and pairs[0] == pairs[1][:: - 1]
