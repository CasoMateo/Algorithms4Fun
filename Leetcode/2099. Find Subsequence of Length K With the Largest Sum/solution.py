class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
      
      priorities = sorted(nums)[len(nums) - k: ]
      result = []
      
      for num in nums:

        if num in priorities:
          result.append(num)
          priorities.remove(num)
      
      return result
