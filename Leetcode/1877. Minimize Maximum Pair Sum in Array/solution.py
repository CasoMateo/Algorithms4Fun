class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        maximum = nums[0] + nums[-1]
        
        prev = nums[0]
        lo = 0 
        hi = -1 
       
        while lo <= len(nums) // 2: 
            lo += 1 
            hi -= 1 
            
            if nums[lo] == prev: 
                continue  
            
            cur = nums[lo] + nums[hi]
            
            maximum = max(maximum, cur)
            prev = nums[lo]
           
        
        return  maximum
