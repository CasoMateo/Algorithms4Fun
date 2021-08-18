class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
      
      if len(trust) < 1:
        if n < 2: 
          return 1 
        return -1
      
      mem = {}
      trusting = set()
      
      for i in range(len(trust)):

        if trust[i][1] in mem: 
          mem[trust[i][1]] += 1 
        else: 
          
          mem[trust[i][1]] = 1 
          
        trusting.add(trust[i][0])
     
 
      pos = max(mem, key = mem.get)
      
      if mem[pos] >= n - 1 and pos not in trusting:
        return pos 
      return -1
