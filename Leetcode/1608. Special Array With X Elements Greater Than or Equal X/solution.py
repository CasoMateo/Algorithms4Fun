class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        nums.sort()
        
        for i in range(len(nums)):
          cur = len(nums) - i
          
          if nums[i] >= cur:
            if i == 0: 
              return cur
              
            if nums[i - 1] < cur:
              return cur
   
        return -1
