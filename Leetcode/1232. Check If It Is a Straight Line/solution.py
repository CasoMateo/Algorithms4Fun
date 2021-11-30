class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
      
      if len(coordinates) == 2: 
        return True
      
      mem = set()
      
      for coordinate in coordinates: 
        mem.add(coordinate[0])
      
      if len(mem) == 1: 
        return True
      
      if len(mem) < len(coordinates):
        return False 
    
      dif = abs(coordinates[1][1] - coordinates[0][1]) / abs(coordinates[1][0] - coordinates[0][0]) 
      
      for i in range(1, len(coordinates)):
        if abs(coordinates[i][1] - coordinates[i - 1][1]) / abs(coordinates[i][0] - coordinates[i - 1][0])  != dif:
          return False
      
      return True
