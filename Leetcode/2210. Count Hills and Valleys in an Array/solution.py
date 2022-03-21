class Solution:
    def countHillValley(self, nums: List[int]) -> int:
    
        i = 1 
        
        while True: 
            if nums[i] == nums[i - 1]: 
                nums = nums[: i] + nums[i + 1: ] 
                i -= 1 
            
            if i == len(nums) - 1:
                break 
            
            i += 1 
        
        count = 0 
        
        for j in range(1, len(nums) - 1): 
            if (nums[j - 1] < nums[j] and nums[j + 1] < nums[j]) or (nums[j - 1] > nums[j] and nums[j + 1] > nums[j]):
                count += 1 
        
        return count 
                
                
    
