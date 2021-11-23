class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
      
      for i in range(len(rectangles)):
        rectangles[i] = min(rectangles[i][0], rectangles[i][1])
      
      return rectangles.count(max(rectangles))
