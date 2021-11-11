class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
      
      intervals = []
      cur = [0]
      
      for i in range(1, len(s)):
        if s[i] != s[i - 1]:
          cur.append(i - 1) 
          if cur[1] - cur[0] >= 2: 
            intervals.append(cur)
          cur = [i]
      
      if len(cur) < 2:
        cur.append(len(s) - 1)
        if cur[1] - cur[0] >= 2:
          intervals.append(cur)
          
      return intervals
