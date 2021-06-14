class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = {}
        pos = float('inf')
        
        for coordinate in points: 
          if x == coordinate[0] or y == coordinate[1]:
            distance = abs(coordinate[0] - x) + abs(coordinate[1] - y)
            if distance < pos:
              pos = distance
              res[distance] = [coordinate]
            elif distance in res: 
              res[distance].append(coordinate)
       
        if pos == float('inf'):
          return -1
        
        for i in range(len(points)): 
          if points[i] in res[pos]:
            return i
        
        return -1
