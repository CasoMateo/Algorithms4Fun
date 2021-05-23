class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums.count(target) == 1:
          return [nums.index(target), nums.index(target)]
          
  
        seen = set()
        for i in range(len(nums)):
          if nums[i] == target: 
            if nums[i] not in seen:
              i1 = i
              seen.add(nums[i])
              break
      
        for j in range(len(nums)):
          if nums[len(nums) - j - 1] == target: 
            i2 = len(nums) - j - 1
            break
            
        if target not in nums:
          return [-1, -1]
        return [i1, i2]
      
      
        
