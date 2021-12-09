class Solution:
    def frequencySort(self, s: str) -> str:
      
      mem = {}
      
      for char in s:
        mem[char] = mem.get(char, 0) + 1 
      
      mem = dict(sorted(mem.items(), key=lambda x: x[1], reverse = True))
      
      decreasing = []
      
      for freq in mem:
        decreasing.extend([freq] * mem[freq])
      
      return decreasing
