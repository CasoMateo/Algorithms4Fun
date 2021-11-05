class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
      
      cur = []
      
      for i in range(len(arr)):
        cur.append(arr[i])
        
        if cur in pieces: 
          pieces.remove(cur)
          cur = []
      
      if pieces:
        return False 
      return True
