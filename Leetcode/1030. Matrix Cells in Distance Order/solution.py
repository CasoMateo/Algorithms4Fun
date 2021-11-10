class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        
      mem = {}
    
      for r in range(rows):
        for c in range(cols):
          if abs(rCenter - r) + abs(cCenter - c) in mem:
            mem[abs(rCenter - r) + abs(cCenter - c)].append([r, c])
          
          else:
            mem[abs(rCenter - r) + abs(cCenter - c)] = [[r, c]]
 
      distance = OrderedDict(sorted(mem.items()))
      
      coordinates = []
      
      for coord in distance: 
        for sep in distance[coord]:
          coordinates.append(sep)
      
      return coordinates
      
      
