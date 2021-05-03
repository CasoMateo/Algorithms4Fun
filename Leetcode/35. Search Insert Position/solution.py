class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      lo = 0 
      hi = len(a) - 1
      
      while lo <= hi: 
        mid = (lo + hi) // 2 
        
        if a[mid] < t: 
          lo = mid + 1 
        elif a[mid] > t: 
          hi = mid - 1 
        else: 
          return mid 
      
      for x in range(len(a) - 1):
        if t > a[x] and t < a[x + 1]:
          return x + 1
      if t < min(a):
        return 0 
      return len(a)
