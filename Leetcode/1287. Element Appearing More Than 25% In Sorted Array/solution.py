
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
      hash_ = {}
      n = len(arr)
      
      for i in arr: 
        hash_[i] = hash_.get(i, 0) + 1

      for num, oc in hash_.items():
        if oc / n > 0.25:
          return num 
