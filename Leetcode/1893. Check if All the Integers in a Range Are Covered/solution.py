class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
      
        for i in range(left, right + 1):
          pos = False
          for j in range(len(ranges)):
            
            if ranges[j][0] <= i and i <= ranges[j][1]:
              pos = True
            
          if not pos: 
            return False
        
        return True
