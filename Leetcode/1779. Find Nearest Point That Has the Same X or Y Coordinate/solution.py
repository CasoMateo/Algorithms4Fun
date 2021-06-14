class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = -1
        pos = float('inf')
        
        for i in range(len(points)): 
          if x == points[i][0] or y == points[i][1]:
            distance = abs(points[i][0] - x) + abs(points[i][1] - y)
            
            if distance < pos:
              pos = distance
              res = i
       
        return res
