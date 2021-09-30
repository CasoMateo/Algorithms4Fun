class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
      
      mem = {}
      
      for num in arr1: 
        mem[num] = mem.get(num, 0) + 1 
      
      new = []
      
      for needed in arr2:
        new.extend([needed] * mem[needed]) 
      
      missing = sorted(set(arr1) - set(arr2))
      
      for mis in missing:
        new.extend([mis] * mem[mis])
      
      return new
        
