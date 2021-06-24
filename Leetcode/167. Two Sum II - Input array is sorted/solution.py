class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      mem = {}
      
      for i in range(len(numbers)):
        comp = target - numbers[i]
        if comp in mem: 
          return [mem[comp] + 1, i + 1]
        else:
          mem[numbers[i]] = i
