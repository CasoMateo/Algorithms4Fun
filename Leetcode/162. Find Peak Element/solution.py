class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
      
      if len(nums) == 1: 
        return 0
      
      if nums[0] > nums[1]:
        return 0 
      
      if nums[-1] > nums[-2]:
        return len(nums) - 1
      
      lo = 1
      hi = len(nums) - 2
      
      while lo <= hi: 
        
        mid = (lo + hi) // 2 
        
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
          return mid 
        
        elif nums[mid] < nums[mid - 1]:
          hi = mid 
        
        elif nums[mid] < nums[mid + 1]:
          lo = mid + 1
      
      
          
        
