class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
      arr.sort()
      minimum = float('inf')
      
      for i in range(1, len(arr)):
 
         minimum = min(minimum, arr[i] - arr[i - 1])
      
      pairs = []
      
      for j in range(1, len(arr)):
        
        if arr[j] - arr[j - 1] == minimum: 
          pairs.append([arr[j - 1], arr[j]])
      
      return pairs
