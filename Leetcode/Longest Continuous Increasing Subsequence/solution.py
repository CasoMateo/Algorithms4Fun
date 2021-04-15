class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
      
      longest = 1
      cur = 1 
      
      if not nums: 
        return 0 
      
      for i in range(1, len(nums)): 
        if nums[i - 1] < nums[i]: 
          cur += 1
          longest = max(longest, cur)
        elif i > len(nums) // 2: 
          break
        else: 
          cur = 1 
          
      return longest
      
