class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        if 1 not in nums: 
          return True
        
        prev = nums.index(1)
        
        for i in range(prev + 1, len(nums)):
          if nums[i] == 1: 
            if i - prev - 1 < k: 
              return False   
            prev = i 
          
        return True
        
        
        
