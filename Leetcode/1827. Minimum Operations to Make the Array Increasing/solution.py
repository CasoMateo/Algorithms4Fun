class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        if len(nums) == 1: 
          return 0 
        
        operations = 0 
        
        for i in range(1, len(nums)):
          if nums[i - 1] >= nums[i]:
            operations += nums[i - 1] - nums[i] + 1
            nums[i] += nums[i - 1] - nums[i] + 1
   
        return operations
            
