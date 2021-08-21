class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        mem = {} 
        cur = 0 
        
        for rank in sorted(set(arr)):
          cur += 1 
          mem[rank] = cur 
            
        for i in range(len(arr)):
          arr[i] = mem[arr[i]]
        
        return arr
