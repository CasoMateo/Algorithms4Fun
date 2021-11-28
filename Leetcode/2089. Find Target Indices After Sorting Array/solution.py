class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
      
      indices = []
      nums.sort()
      
      for index in range(len(nums)):
        if nums[index] > target: 
          break
        
        if nums[index] == target: 
          indices.append(index)
      
      return indices
