class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
      
      for i in range(len(nums)):
        if -nums[i] in nums[:i]:
          return nums[i]
        else: 
          temp = nums[i]
          nums[i] = -temp 
        
