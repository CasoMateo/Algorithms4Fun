class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
      
      integer = ''
      
      for digit in num: 
        integer += str(digit)
      
      integer = int(integer) + k
      
      new = []
      
      for digit in str(integer):
        new.append(int(digit))
      
      return new
