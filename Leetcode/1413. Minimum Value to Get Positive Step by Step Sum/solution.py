class Solution:
    def minStartValue(self, nums: List[int]) -> int:
      
      s = largest = 0 
      
      for i in range(len(nums)):
        
        s += nums[i]
        
        if s < 1: 
          largest = min(largest, s) 
      
      return 1 - largest
          
        
