class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
      
      years = []
      
      for x in range(len(logs)):
        years.extend(range(logs[x][0], logs[x][1]))

      mem = {}
      
      for y in years: 
        mem[y] = mem.get(y, 0) + 1
    
      year = tot = 0 
      
      for freq in mem: 
        if mem[freq] > tot or (mem[freq] == tot and year > freq): 
          year = freq 
          tot = mem[freq]

      return year
