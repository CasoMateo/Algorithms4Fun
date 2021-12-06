class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
      
      minutes = []
      
      for i in range(len(timePoints)):
        cur = (int(timePoints[i][0] + timePoints[i][1]) * 60) + int(timePoints[i][3] + timePoints[i][4]) + 1
        minutes.append(cur)
      
      minutes.sort()
      dif = float('inf')
            
      for j in range(1, len(minutes)):
        ac = minutes[j] - minutes[j - 1]
        reverse = (1440 - minutes[j]) + minutes[j - 1]
        dif = min(dif, reverse, ac)
      
      dif = min(dif, 1440 - minutes[-1] + minutes[0])
      return dif
          
