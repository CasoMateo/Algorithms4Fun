class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
      
      mem = {}
      
      for i in range(len(nums)):
        if nums[i] not in mem: 
          mem[nums[i]] = i
        else: 
          if abs(i - mem[nums[i]]) <= k:
            return True 
          mem[nums[i]] = i
      return False
