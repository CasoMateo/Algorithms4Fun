class Solution:
    def findComplement(self, num: int) -> int:
      
      mem = {'0' : '1', '1' : '0'}
      
      initial = list(bin(num))
      
      for i in range(2, len(initial)):
        initial[i] = mem[initial[i]]
        
      return int(''.join(initial), 2)

