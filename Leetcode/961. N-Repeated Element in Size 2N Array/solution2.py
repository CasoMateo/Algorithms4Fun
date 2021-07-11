class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
      
      mem = set()
      
      for num in nums: 
        if num in mem: 
          return num 
        else: 
          mem.add(num)
