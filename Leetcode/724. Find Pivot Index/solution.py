class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
      cur = 0
      s = sum(nums)
      
      for i in range(len(nums)):
        if cur == s - cur - nums[i]:
          return i
        cur += nums[i]
          
      return -1
