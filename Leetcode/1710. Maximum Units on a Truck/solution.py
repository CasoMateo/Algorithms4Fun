class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        mem = {}
        
        for i in range(len(boxTypes)):
          mem[boxTypes[i][1]] = mem.get(boxTypes[i][1], 0) + boxTypes[i][0]
        
        priorities = dict(sorted(mem.items(), key = operator.itemgetter(0), reverse = True))
        
        accum = 0 
       
        for boxes in priorities: 

          if priorities[boxes] > truckSize: 
            accum += boxes * truckSize
            break
          
          else:
            accum += priorities[boxes] * boxes
            truckSize -= priorities[boxes]
            
            if truckSize == 0: 
              break
        
        return accum
            
