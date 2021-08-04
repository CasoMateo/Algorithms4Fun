class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        mem = {}
        
        for num in arr: 
          mem[num] = mem.get(num, 0) + 1
          
        return len(mem) == len(set(mem.values()))
        
