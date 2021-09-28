
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
      
      mem = {}
      
      for i in range(len(nums)):
        if nums[i] not in mem: 
  
          mem[nums[i]] = [1, i]
      
        else: 
          if nums[i] not in nums[i + 1: ]:
            mem[nums[i]][1] = i - mem[nums[i]][1] 
          
          mem[nums[i]][0] += 1 
     
      m = nums[0]
      
      for freq in mem: 
        if mem[freq][0] > mem[m][0]:
          m = freq
        
        elif mem[freq][0] == mem[m][0]:
          if mem[freq][1] < mem[m][1]:
            m = freq
      
      return mem[m][1] + 1
