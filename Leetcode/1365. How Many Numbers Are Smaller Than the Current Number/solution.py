from collections import Counter

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
      smaller = []
      ref = sorted(set(nums))
      mem = Counter(nums)
      freq = {}
      cur = 0
      
      for i in range(len(ref)):
        freq[ref[i]] = cur 
        cur += mem[ref[i]]
      
      for j in range(len(nums)):
        smaller.append(freq[nums[j]])
      
      return smaller
      
      
      
