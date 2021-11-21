class Solution:
    def maxDistance(self, colors: List[int]) -> int:
      
      longest = 0
      
      for i in range(len(colors)):
        if colors[i] != colors[0] or colors[i] != colors[-1]: 
          longest = max(longest, i, len(colors) - 1 - i)
      
      return longest
