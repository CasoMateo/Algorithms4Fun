class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
      ranges = []
      cur = []
      
      for i in range(len(nums)):
        cur.append(nums[i])
        if nums[i] + 1 not in nums:
          ranges.append(cur)
          cur = []
      
      formatted = []
      
      for ran in ranges: 
        
        if len(ran) == 1: 
          formatted.append(str(ran[0]))
        
        else: 
          formatted.append(str(ran[0]) + '->' + str(ran[-1]))
      
      return formatted
