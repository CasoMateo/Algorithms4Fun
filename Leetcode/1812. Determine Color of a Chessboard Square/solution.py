class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
      
      if ord(coordinates[0]) % 2 == 1 and int(coordinates[1]) % 2 == 0:
        return True
 
      elif ord(coordinates[0]) % 2 == 0 and int(coordinates[1]) % 2 == 1:
        return True
      
      return False
