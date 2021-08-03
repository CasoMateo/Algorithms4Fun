class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            
            cur = nums[ : i] + nums[i + 1:]
            increasing = True
            
            for j in range(1, len(cur)):
                if cur[j] <= cur[j - 1]:
                    increasing = False
            
            if increasing:
              return True
        
        return False
