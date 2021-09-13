class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
      
      for i in range(len(rectangles)):
        rectangles[i] = rectangles[i][0] / rectangles[i][1]
      
      mem = {}
      
      for rectangle in rectangles: 
        mem[rectangle] = mem.get(rectangle, 0) + 1 
      
      accum = 0 
      
      for freq in mem: 
        if mem[freq] >= 2:
          accum += mem[freq] * (mem[freq] - 1)
      
      return accum // 2
        
