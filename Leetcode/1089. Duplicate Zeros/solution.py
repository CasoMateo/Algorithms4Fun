class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        last = False
        initial = len(arr)
        
        for i in range(len(arr)):
          if last: 
            last = False 
            arr.insert(i - 1, 0)
          elif arr[i] == 0:
            last = True

        for j in range(len(arr) - initial):
          arr.pop()
             
        
