class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
      
        difference = sorted(arr, key = lambda item: abs(x - item))

        cĺosest = []
        for i in range(k):
            closest.append(difference[i])
        
        return sorted(closest)
