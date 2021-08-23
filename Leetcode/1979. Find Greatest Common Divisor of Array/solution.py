class Solution:
    def findGCD(self, nums: List[int]) -> int:

      for i in range(min(nums)):
        
        if max(nums) % (min(nums) - i) == 0 and min(nums) % (min(nums) - i) == 0: 
          return min(nums) - i
        

        
        
