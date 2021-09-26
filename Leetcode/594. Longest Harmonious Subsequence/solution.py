from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
      
      nums.sort() 
      mem = Counter(nums)
      largest = 0
      
      for i in range(len(nums)):
        if nums[i] + 1 in mem: 
          largest = max(largest, mem[nums[i]] + mem[nums[i] + 1])
      
      return largest 
          
        
            
        
        
        
