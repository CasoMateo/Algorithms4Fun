class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      
      new = sorted(set(nums))
      
      longest = cur = 1 
      
      if not nums: 
        return 0
      
      for i in range(1, len(new)):
        if new[i] - new[i - 1] == 1:
          cur += 1 
          longest = max(longest, cur)
        else: 
          cur = 1 
      
      return longest
          
