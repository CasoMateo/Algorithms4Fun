class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
      bar = max(nums) // 2 

      for num in nums:
        if num > bar and num != max(nums): 
          return -1
      return nums.index(max(nums))
      
