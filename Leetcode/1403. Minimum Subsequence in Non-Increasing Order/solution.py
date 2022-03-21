class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        
        total = sum(nums) 
        
        nums.sort(reverse = True)
        cur = 0 
        
        for n in range(len(nums)): 
            cur += nums[n]
            if cur > total - cur: 
                return nums[: n + 1]
        
            
        
