class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
      
      if start > destination:
        start, destination = destination, start 
      
      rem1 = 0 
      for i in range(start, destination):
        rem1 += distance[i]
        
      rem2 = 0
      for j in range(destination, len(distance) + start):
        rem2 += distance[j % len(distance)]
      
      return min(rem1, rem2)
