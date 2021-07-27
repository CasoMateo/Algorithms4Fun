class Solution:
    def check(self, nums: List[int]) -> bool:
      
      original = sorted(nums)
      
      for i in range(len(nums)):
        cur = nums[len(nums) - i - 1:] + nums[: len(nums) - i - 1] 
        
        if cur == original: 
          return True 
      
      return False
    
