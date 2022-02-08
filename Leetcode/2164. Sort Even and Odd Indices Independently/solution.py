class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        even = []
        odd = []
        
        for cur in range(len(nums)):
            if cur == 0 or cur % 2 == 0: 
                even.append(nums[cur])
            
            else: 
                odd.append(nums[cur])
        
        even.sort()
        odd.sort(reverse = True)
        nums = []
        
        for ac in range(len(even)):
            nums.append(even[ac])
            if ac <= len(odd) - 1:
                nums.append(odd[ac])
        
        return nums
        
