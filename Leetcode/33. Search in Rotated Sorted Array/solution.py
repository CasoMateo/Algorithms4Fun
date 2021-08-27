class Solution:
    def search(self, nums: List[int], target: int) -> int:
          
        shifted = len(nums) - nums.index(max(nums))
        nums = nums[-shifted + 1: ] + nums[: len(nums) - shifted + 1]
       
        lo = 0
        hi = len(nums) - 1
        index = -1
        
        while lo <= hi: 
          mid = (lo + hi) // 2 
          
          if nums[mid] > target: 
            hi = mid - 1
          
          elif nums[mid] < target: 
            lo = mid + 1
          
          else: 
            index = mid 
            break
        
        if index == -1:
          return -1
        
        return (index - shifted + 1) % len(nums)
            
          
