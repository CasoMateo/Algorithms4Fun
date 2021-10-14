class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
      
      nums.sort()
      
      accum = 0 
      
      for i in range(0, len(nums), 2):
        accum += nums[i]
      
      return accum
        
