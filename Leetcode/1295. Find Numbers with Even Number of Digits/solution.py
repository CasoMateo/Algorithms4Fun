class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        ev = 0 
        
        for num in nums: 
          if len(str(num)) % 2 == 0: 
            ev += 1 
        
        return ev
