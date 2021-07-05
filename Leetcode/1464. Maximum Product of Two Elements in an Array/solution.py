class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      
      return (sorted(nums)[-1] - 1) * (sorted(nums)[-2] - 1) 
    
      # Finding the two biggest elements in O(Nlog(N)), but this could be done in O(N) time.
      
