class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        mem = {}
        
        for num in arr: 
          mem[num] = mem.get(num, 0) + 1
          
        priorities = []
        
        for freq in mem:
          priorities.append(mem[freq])
        
        priorities.sort(reverse = True)
        i = accum = 0
    
        while True: 
          i += 1
          accum += priorities[i - 1]
          if accum >= len(arr) / 2: 
            return i
