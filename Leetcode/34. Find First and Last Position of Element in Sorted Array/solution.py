class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
          return [-1, -1]
          
        for i in range(len(nums)):
          if nums[i] == target: 
            i1 = i
            break
            
        for j in range(len(nums)):
          if nums[len(nums) - j - 1] == target: 
            i2 = len(nums) - j - 1
            break
        return [i1, i2]
      
      
        
