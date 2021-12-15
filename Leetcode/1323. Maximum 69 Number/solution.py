class Solution:
    def maximum69Number (self, num: int) -> int:
      
      num = str(num)
      longest = int(num) 
      mem = {'6': '9', '9': '6'}
      
      for i in range(len(num)):
        cur = num[: i] + mem[num[i]] + num[i + 1: ]
        
        longest = max(longest, int(cur))
      
      return longest
