class Solution:
    def trimMean(self, arr: List[int]) -> float:
      
      arr.sort()
      cur = len(arr) // 20
      
      removed = sum(arr) - sum(arr[: cur]) - sum(arr[len(arr) - cur: ])
      
      return removed / (len(arr) - 2 * cur)
