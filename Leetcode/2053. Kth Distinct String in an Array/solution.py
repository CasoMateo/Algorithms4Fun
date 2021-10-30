
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        mem = {}
        
        for num in arr: 
          mem[num] = mem.get(num, 0) + 1
        
        for i in range(len(arr)):
          if mem[arr[i]] == 1 and k == 1: 
            return arr[i]
          
          elif mem[arr[i]] == 1: 
            k -= 1 
          
        return ''
