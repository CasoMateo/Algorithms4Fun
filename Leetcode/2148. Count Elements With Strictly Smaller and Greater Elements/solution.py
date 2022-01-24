class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        count = 0 
        
        for i in range(len(nums)):
            if nums[i] > min(nums) and nums[i] < max(nums):
                count += 1 
        
        return count
