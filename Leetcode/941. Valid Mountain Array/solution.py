class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3 or arr[1] < arr[0]:
          return False
      
        peak = False
        for i in range(1, len(arr)):
          if arr[i] > arr[i - 1] and peak: 
             return False 
            
          if arr[i] == arr[i - 1]:
            return False 
          
          elif arr[i] < arr[i - 1]:
            if not peak: 
              peak = True
          
        if not peak: 
          return False
        
        return True
            
