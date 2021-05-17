class Solution(object):
    def runningSum(self, nums):
      cur = 0 
      res = []
      
      for i in nums: 
        cur += i 
        res.append(cur)
      
      return res
        
