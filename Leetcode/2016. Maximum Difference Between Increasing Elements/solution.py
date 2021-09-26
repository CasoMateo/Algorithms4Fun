class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        longest = -1
        
        for i in range(len(nums) - 1):
          if max(nums[i + 1: ]) <= nums[i]:
            continue 
            
          longest = max(longest, max(nums[i + 1: ]) - nums[i])
        
        return longest
