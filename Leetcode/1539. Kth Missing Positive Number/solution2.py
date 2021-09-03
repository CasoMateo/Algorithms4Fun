class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
      
      needed = set(range(1, len(arr) + k + 1))
        
      difference = list(needed - set(arr))
      difference.sort()
      
      return difference[k - 1]
