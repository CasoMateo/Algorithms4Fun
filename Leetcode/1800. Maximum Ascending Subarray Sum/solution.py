class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
      largest = cur = nums[0]
      
      for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
          cur += nums[i]
        
        else:
          largest = max(largest, cur)
          cur = nums[i]
      
      largest = max(largest, cur)
      return largest
