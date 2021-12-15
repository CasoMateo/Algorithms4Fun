class Solution:
    def fib(self, n: int) -> int:
      
      if n == 0: 
        return 0
      
      series = [0, 1, 1]
      
      for i in range(3, n + 1):
        if i + 1 > len(series):
          series.append(series[-2] + series[-1])

      return series[-1]
