class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        cur = sum(nums[: k])
        longest = cur 

        for i in range(k, len(nums)):
         
          cur += nums[i] - nums[i - k] 
          longest = max(longest, cur)

        return longest / k
