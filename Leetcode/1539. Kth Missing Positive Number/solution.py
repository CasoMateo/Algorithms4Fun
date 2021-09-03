class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
      
      cur = 0 
      
      for i in range(1, len(arr) + k + 1):
        if i not in arr: 
          cur += 1 

        if cur == k: 
          return i 
