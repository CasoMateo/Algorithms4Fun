class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
      
      mem = {}
      groups = []
      
      for i in range(len(groupSizes)):
        if groupSizes[i] in mem: 
          mem[groupSizes[i]].append(i)
          if len(mem[groupSizes[i]]) == groupSizes[i]:
            groups.append(mem[groupSizes[i]])
            mem[groupSizes[i]] = []
        
        else: 
          if groupSizes[i] == 1:
            groups.append([i])
            
          else:
            mem[groupSizes[i]] = [i]
         
      return groups
