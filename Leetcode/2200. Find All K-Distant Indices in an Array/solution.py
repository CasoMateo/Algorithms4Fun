class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
      
      mem = []
      
      for i in range(len(nums)):
        if nums[i] == key: 
          
          mem.append(i)
        
      indices = []
      
      for j in range(len(nums)): 
        for index in mem: 
          if abs(j - index) <= k: 
            indices.append(j)
            break
            
          
      return indices
            
