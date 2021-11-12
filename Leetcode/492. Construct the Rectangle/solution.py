from math import sqrt

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
      
      for i in range(int(sqrt(area)) + 1, 0, -1):
        if area % i == 0: 
          return sorted([i, area // i], reverse = True)
        
