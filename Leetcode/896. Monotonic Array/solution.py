class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        return self.monotone(nums) or self.monotone(nums[:: -1])
       
    
    def monotone(self, nums):
       
        forward = True 
        
        for i in range(1, len(nums)):
          if nums[i -  1] > nums[i]:
            forward = False 
        
        return forward
