
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        
        res = 0
        
        for i in range(1, len(points)):
            cur = points[i]
            prev = points[i - 1]
            x_dif = abs(cur[0] - prev[0])
            y_dif = abs(cur[1] - prev[1])
            res += max(x_dif, y_dif)
        
        return res
        
