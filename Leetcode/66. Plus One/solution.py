class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      
      integer = ''
      
      for digit in digits: 
        integer += str(digit)
      
      integer = int(integer) + 1
      
      new = []
      
      for digit in str(integer):
        new.append(int(digit))
      
      return new
