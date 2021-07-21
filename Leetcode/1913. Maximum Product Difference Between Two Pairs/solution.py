import sys

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
  
      last = max(nums)
      first = min(nums)
      nums.remove(last)
      nums.remove(first)
      almost = max(nums)
      second = min(nums)
      
      return (almost * last) - (first * second)
    
