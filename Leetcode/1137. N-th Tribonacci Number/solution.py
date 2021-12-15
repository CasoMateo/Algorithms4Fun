class Solution:
    def tribonacci(self, n: int) -> int:
      
      series = [0, 1, 1]
      
      if n <= 2:
        return series[n]
      
      for i in range(4, n + 2):
        if len(series) < i: 
          series.append(series[-3] + series[-2] + series[-1])

      return series[-1]
