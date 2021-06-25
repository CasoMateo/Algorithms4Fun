class Solution:
    def maxArea(self, height: List[int]) -> int:
      longest = 0
      lo = 0 
      hi = len(height) - 1
      
      while lo <= hi: 
        cur = 0 
        cur = (hi - lo) * min(height[lo], height[hi])
        longest = max(longest, cur)
        
        if height[lo] <= height[hi]:
          lo += 1 
        else: 
          hi -= 1
      return longest
          
