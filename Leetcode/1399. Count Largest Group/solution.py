class Solution:
    def countLargestGroup(self, n: int) -> int:
      
      groups = {}
      
      for num in range(1, n + 1):
        cur = 0 
        for sep in str(num):
          cur += int(sep)

        groups[cur] = groups.get(cur, 0) + 1
      
      largest = max(groups.values())
      count = 0 
      
      for pos in groups: 
        if groups[pos] == largest: 
          count += 1 
      
      return count
