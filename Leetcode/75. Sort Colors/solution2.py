class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        freq_0 = freq_1 = freq_2 = 0 
        
        if 0 in nums: 
          freq_0 = nums.count(0)
        if 1 in nums:
          freq_1 = nums.count(1)
        if 2 in nums:
          freq_2 = nums.count(2)
          
        cur = 0 
        
        if freq_0 != 0: 
          for times in range(freq_0):
            nums[cur] = 0 
            cur += 1
          
        if freq_1 != 0:
          for times in range(freq_1):
            nums[cur] = 1
            cur += 1
          
        if freq_2 != 0: 
          for times in range(freq_2):
            nums[cur] = 2
            cur += 1
          
      
        
          
