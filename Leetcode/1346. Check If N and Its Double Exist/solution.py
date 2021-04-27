class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
      arr.sort()
      
      for i in range(len(arr)): 
        complement = arr[i] / 2 
        if self.binary_search(arr, complement) is not False: 
          if self.binary_search(arr, complement) != i: 
            return True 
          
      return False
    
    def binary_search(self, arr, t):
      
      lo = 0 
      hi = len(arr) - 1 
      
      while lo <= hi: 
        mid = (lo + hi) // 2 
        if arr[mid] < t: 
          lo = mid + 1 
        elif arr[mid] > t: 
          hi = mid - 1 
        else: 
          return mid 
      return False
  
      
